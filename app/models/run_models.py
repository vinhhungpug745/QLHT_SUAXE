import hashlib
from app.models.model import *

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        # db.drop_all()
        # db.create_all()
        # c1 = Category(name="Moto")
        # c2 = Category(name="Oto")
        # db.session.add_all([c1, c2])
        #
        # b1 = Brand(name="Honda")
        # b2 = Brand(name="Yamaha")
        # b3 = Brand(name="Toyota")
        # b4 = Brand(name="Mercedes")
        # db.session.add_all([b1, b2,b3,b4])
        #
        #
        # with open("data/component.json", encoding="utf-8") as f:
        #     components = json.load(f)
        #
        #     for c in components:
        #         comp = Component(**c)
        #         db.session.add(comp)
        #
        # db.session.commit()

        admin_pass = str(hashlib.md5(("admin").encode('utf-8')).hexdigest())
        new_admin = User(
            name="Quản trị viên",
            username="admin",
            password=admin_pass,
            avatar="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTfjno7hGrNNuPZwaFZ8U8Mhr_Yq39rzd_p0YN_HVYk6KFmMETjtgd9bwl0UhU6g4xDDGg&usqp=CAU",
            user_role=UserRole.ADMIN

        )
        db.session.add(new_admin)
        db.session.commit()
