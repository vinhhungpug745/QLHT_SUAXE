from flask import Flask, render_template, request
from app.models import dao


class ComponentController:

    # [GET] /components
    def index(self):
        args = request.args.to_dict()
        q=request.args.get('q')
        cate_id = request.args.get("cate_id")
        brand_id = request.args.get("brand_id")
        comps=dao.load_component(q=q,cate_id=cate_id,brand_id=brand_id)
        cates=dao.load_category()
        brands=dao.load_brand()
        selected_cate_name = "Loại linh kiện"
        if cate_id and cate_id.isdigit():
            selected_cate = next((c for c in cates if c.id == int(cate_id)), None)
            if selected_cate:
                selected_cate_name = selected_cate.name

        selected_brand_name = "Hãng linh kiện"
        if brand_id and brand_id.isdigit():
            selected_brand = next((b for b in brands if b.id == int(brand_id)), None)
            if selected_brand:
                selected_brand_name = selected_brand.name
        return render_template("components.html", page="Linh kiện",
                               comps=comps,cates=cates,brands=brands,current_args=args,
                               selected_cate_name=selected_cate_name,
                               selected_brand_name=selected_brand_name)


    # [GET] /components/:slug
    def show(self, slug):
        return render_template("componentDetail.html", slug=slug)
