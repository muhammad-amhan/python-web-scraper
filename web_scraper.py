
import requests
from bs4 import BeautifulSoup


class FetchProductInfo(object):

    def __init__(self):
        self.url = 'https://www.humblebundle.com/games/bandai-namco-bundle-3?hmb_source=navbar&hmb_medium=product_tile&hmb_campaign=tile_index_2'
        self.products_info_dict = {}
        self.get_offers()

    def get_offers(self):
        req = requests.get(self.url)
        soup = BeautifulSoup(req.text, 'html.parser')

        products_blocks = soup.select('.dd-game-row')

        for products_block in products_blocks:
            products_headline = products_block.select('.dd-header-headline')
            if products_headline:
                stripped_headline = products_headline[0].text.strip()
                products = [product.text.strip() for product in products_block.select('.dd-image-box-caption')]

                self.products_info_dict[stripped_headline] = {
                    'products': products
                }

        self.response_to_str()

    def response_to_str(self):
        for product_headline, products_info in self.products_info_dict.items():
            print(f'{product_headline}')
            print('Products:')
            print('{1} {0}'.format('\n\t* '.join(products_info['products']), '\t*'))
            print('\n')


if __name__ == '__main__':
    request = FetchProductInfo()

