#!/usr/bin/python3

from flask_login import login_required, current_user
from flask import Blueprint, render_template, request, redirect, url_for, flash

from app.models.merchant import Merchant
from app.models.product import Product, ProductCategory, ProductImage
from app.models.order import Order
from app.models.address import Address
from app.utils.constants import (
    USER_FIELDS,
    ADDRESS_FIELDS,
    PRODUCT_FIELDS,
    PRODUCT_IMAGE_FIELDS,
    MEDIA_PATH,
)
from app.utils.decorators import is_merchant
from app.utils.validations import validate_extension
from app.utils.helpers import process_image

from config import db

from datetime import datetime
import os
import uuid


merchants = Blueprint("merchant", __name__, url_prefix="/merchant")


@merchants.route("/<merchant_id>", methods=["GET"], strict_slashes=False)
@login_required
@is_merchant
def get_merchant(merchant_id):
    """Get merchant data
    Args:
        merchant_id (string): merchant id
        product_id (string): product id
    """
    merchant = Merchant.query.filter_by(id=merchant_id).first()
    return render_template("merchant/merchant.html", merchant=merchant)


@merchants.route("/<merchant_id>/update", methods=["GET", "POST"], strict_slashes=False)
@login_required
@is_merchant
def update_merchant(merchant_id):
    """Update merchant data
    Args:
        merchant_id (string): merchant id
        product_id (string): product id
    """
    merchant = Merchant.query.filter_by(id=merchant_id).first()

    if request.method == "GET":
        return render_template("merchant/merchant_update.html", merchant=merchant)

    for name in USER_FIELDS:
        if request.form.get(name) is not None:
            setattr(merchant.user, name, request.form.get(name))

    for name in ADDRESS_FIELDS:
        if request.form.get(name) is not None:
            setattr(merchant.merchant_address, name, request.form.get(name))

    db.session.add(merchant)
    db.session.commit()
    flash("Merchant updated successfully.")
    return redirect(url_for("merchant.update_merchant", merchant_id=merchant.id))


@merchants.route("/<merchant_id>/delete", methods=["DELETE"], strict_slashes=False)
@login_required
@is_merchant
def delete_merchant(merchant_id):
    """Get merchant data
    Args:
        merchant_id (string): merchant id
    """
    return render_template("merchant/merchant.html")


@merchants.route("/<merchant_id>/orders", methods=["GET"], strict_slashes=False)
@login_required
@is_merchant
def merchant_orders(merchant_id):
    """Get merchant orders
    Args:
        merchant_id (string): merchant id
    """
    merchant = Merchant.query.filter_by(id=merchant_id).first()

    return render_template(
        "merchant/merchant_orders.html", orders=merchant.merchant_orders
    )


@merchants.route(
    "/<merchant_id>/orders/<order_id>", methods=["GET"], strict_slashes=False
)
@login_required
@is_merchant
def merchant_order(merchant_id, order_id):
    """Get merchant single order
    Args:
        merchant_id (string): merchant id
        product_id (string): product id
    """
    page = request.args.get("page", default=1, type=int)
    orders = (
        Order.query.filter(db.and_(merchant_id == merchant_id, id == order_id))
        .order_by(Order.created_at)
        .paginate(page=page, per_page=15)
    )
    return render_template("merchant/merchant_orders.html", orders=orders)


@merchants.route("/<merchant_id>/products", methods=["GET"], strict_slashes=False)
@login_required
@is_merchant
def merchant_products(merchant_id):
    """Get merchant products
    Args:
        merchant_id (string): merchant id
    """
    page = request.args.get("page", default=1, type=int)
    query = request.args.get("query", default="", type=str)

    products = (
        Product.query.filter(
            Product.merchant_id == merchant_id,
            Product.title.ilike(r"%{}%".format(query)),
        )
        .order_by(Product.created_at)
        .paginate(page=page, per_page=10)
    )

    return render_template("merchant/merchant_products.html", products=products)


@merchants.route(
    "/<merchant_id>/products/add", methods=["GET", "POST"], strict_slashes=False
)
@login_required
@is_merchant
def merchant_add_product(merchant_id):
    """Get merchant products
    Args:
        merchant_id (string): merchant id
    """
    merchant = Merchant.query.filter_by(id=merchant_id).first()
    categories = ProductCategory.query.all()

    if request.method == "GET":
        return render_template(
            "merchant/merchant_add_product.html",
            categories=categories,
            merchant=merchant,
        )

    product = Product()
    product_image = ProductImage()
    category = ProductCategory.query.filter_by(
        id=request.form.get("category", "")
    ).first()

    for name in PRODUCT_FIELDS:
        if request.form.get(name) is not None:
            setattr(product, name, request.form.get(name))

    file = request.files.get("product_image")
    if len(request.files) > 0 and (file and file.filename != ""):
        image = process_image(file)

        if len(image) == 0:
            return render_template(
                "merchant/merchant_update_product.html",
                categories=categories,
                merchant=merchant,
                product=product,
            )

        setattr(product_image, "name", image.get("name"))
        setattr(product_image, "file_path", image.get("path"))

    if product_image.name and product_image.file_path:
        setattr(product, "images", product_image)
        db.session.add(product_image)
    else:
        return render_template(
            "merchant/merchant_add_product.html",
            categories=categories,
            merchant=merchant,
        )

    category.products.append(product)
    merchant.products.append(product)
    db.session.add(category)
    db.session.add(merchant)
    db.session.add(product)
    db.session.commit()

    return render_template(
        "merchant/merchant_add_product.html", categories=categories, merchant=merchant
    )


@merchants.route(
    "/<merchant_id>/products/<product_id>/update",
    methods=["GET", "POST"],
    strict_slashes=False,
)
@login_required
@is_merchant
def merchant_update_product(merchant_id, product_id):
    """Get merchant products
    Args:
        merchant_id (string): merchant id
    """

    merchant = Merchant.query.filter_by(id=merchant_id).first()
    product = Product.query.filter_by(id=product_id, merchant_id=merchant_id).first()
    categories = ProductCategory.query.all()

    if request.method == "GET":
        return render_template(
            "merchant/merchant_update_product.html",
            categories=categories,
            merchant=merchant,
            product=product,
        )

    product_image = ProductImage()
    category = ProductCategory.query.filter_by(
        id=request.form.get("category", "")
    ).first()
    
    for name in PRODUCT_FIELDS:
        if request.form.get(name) is not None:
            setattr(product, name, request.form.get(name))

    file = request.files.get("product_image")
    if len(request.files) > 0 and (file and file.filename != ""):
        image = process_image(file)

        if len(image) == 0:
            return render_template(
                "merchant/merchant_update_product.html",
                categories=categories,
                merchant=merchant,
                product=product,
            )

        setattr(product_image, "name", image.get("name"))
        setattr(product_image, "file_path", image.get("path"))

    if product_image.name and product_image.file_path:
        if product.images:
            os.unlink(os.path.join(MEDIA_PATH, product.images.file_path))
            db.session.delete(product.images)

        setattr(product, "images", product_image)
        db.session.add(product_image)
        
    if category:
        category.products.append(product)
    db.session.add(product)
    db.session.commit()

    return render_template(
        "merchant/merchant_update_product.html",
        categories=categories,
        merchant=merchant,
        product=product,
    )


@merchants.route(
    "/<merchant_id>/products/<product_id>/delete",
    methods=["GET"],
    strict_slashes=False,
)
@login_required
@is_merchant
def merchant_delete_product(merchant_id, product_id):
    """Delete merchant product
    Args:
        merchant_id (string): merchant id
    """

    merchant = Merchant.query.filter_by(id=merchant_id).first()
    product = Product.query.filter_by(id=product_id, merchant=merchant).first()

    if product is None:
        print("not found")
        return redirect(url_for("merchant.merchant_products", merchant_id=merchant_id))

    if product.merchant != merchant:
        return redirect(url_for("merchant.merchant_products", merchant_id=merchant_id))

    os.unlink(
        os.path.join(MEDIA_PATH, product.images.file_path)
    )  # delete file from path
    db.session.delete(product.images)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for("merchant.merchant_products", merchant_id=merchant_id))


@merchants.route("/<merchant_id>/customers", methods=["GET"], strict_slashes=False)
@login_required
@is_merchant
def merchant_customers(merchant_id):
    """Get merchant customers
    Args:
        merchant_id (string): merchant id
    """
    page = request.args.get("page", default=1, type=int)
    query = request.args.get("query", default="", type=str)

    products = (
        Product.query.filter(
            merchant_id == merchant_id, Product.title.ilike(r"%{}%".format(query))
        )
        .order_by(Product.created_at)
        .paginate(page=page, per_page=15)
    )
    return render_template("merchant/merchant_customers.html", products=products)
