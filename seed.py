from faker import Faker
from blog import db
from blog.models import Post


def generate_posts(how_many=10):
    fake = Faker()

    for _ in range(how_many):
        post = Post(
            title=fake.sentence(),
            content="\n".join(fake.paragraphs(5))
        )

        db.session.add(post)

    db.session.commit()

    print(f"Dodano {how_many} postów.")