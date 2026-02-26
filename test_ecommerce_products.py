#To run ALL scenarios in feature, use this code
#from pytest_bdd import scenarios

#scenarios("features/eCommerce.feature")

#Or you could list each one individually
from pytest_bdd import scenario

#@scenario("features/eCommerce.feature", "Ecommerce products delivery")
#def test_products():
#    pass

#@scenario("features/eCommerce.feature", "Ecommerce shopping page, change values on checkout page")
#def test_checkout():
#    pass

#Or you could just run one scenario per file, this is more likely when developing, with one of the
# other options more likely for production
@scenario("features/eCommerce.feature", "Ecommerce products delivery")
def test_ecommerce_products():
    pass






