import pytest

from ecommerce.user.models import User


@pytest.fixture(autouse=True)
def create_dummy_user(tmpdir):
    from conf_test_db import override_get_db
    database = next(override_get_db())
    new_user = User(name='Vladelo', email='vladelo@gmail.com', password='vladelo123')
    database.add(new_user)
    database.commit()

    yield

    # Teardown : fill with any logic you want
    database.query(User).filter(User.email == 'vladelo@gmail.com').delete()
    database.commit()
