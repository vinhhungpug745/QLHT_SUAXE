import hashlib
from app.models.model import Category, Brand, Component,User,UserRole
from app._init_ import create_app,db

def load_category():
    # with open("data/category.json", 'r', encoding='utf-8') as f:
    #     return json.load(f)
    return Category.query.all()

def load_brand():
    return Brand.query.all()

def load_component(q=None, cate_id=None, brand_id=None):
    # with open("data/component.json", 'r', encoding='utf-8') as f:
    #     component = json.load(f)
    #     if q:
    #         component = [c for c in component if c["name"].find(q)>=0]
    #     if cate_id:
    #         component = [c for c in component if c["cate_id"].__eq__(int(cate_id))]
    #     if brand_id:
    #         component = [c for c in component if c["brand_id"].__eq__(int(brand_id))]
    #     return component
    query = Component.query
    if q:
        query = query.filter(Component.name.contains(q))

    if cate_id:
        query = query.filter(Component.cate_id.__eq__(int(cate_id)))

    if brand_id:
        query = query.filter(Component.brand_id.__eq__(int(brand_id)))

    # if page:
    #     size = app.config["PAGE_SIZE"]
    #     start = (int(page)-1)*size
    #     query = query.slice(start, (start+size))

    return query.all()

def add_user(name, username, password, **kwargs):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    user = User(name=name.strip(),
                username=username.strip(),
                password=password,
                avatar=kwargs.get('avatar'))
    db.session.add(user)
    db.session.commit()

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def check_login(username, password,role=UserRole.USER):
    if username and password:
        password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
        return User.query.filter(User.username.__eq__(username.strip()),
                                 User.password.__eq__(password.strip()),
                                 User.user_role.__eq__(role)).first()


def count_cart(cart):
    total_quantity, total_amount = 0, 0

    if cart:
        for c in cart.values():
            total_quantity += c['quantity']
            total_amount += c['quantity'] * c['price']

    return {
        'total_quantity': total_quantity,
        'total_amount': total_amount
    }
if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        print(load_category())
        print(load_brand())
        print(load_component())

