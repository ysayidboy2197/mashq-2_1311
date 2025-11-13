class Product:
    def __init__(self, nom, narx, zaxira):
        self.nom = nom
        self.narx = narx
        self.__zaxira = zaxira

    def get_info(self):
        status = f"Zaxira: {self.__zaxira}" if self.__zaxira > 0 else "Sotuvda yo‘q"
        return f"{self.nom} - {self.narx} so‘m | {status}"

    def purchase(self, miqdor):
        if self.__zaxira <= 0:
            print(f"{self.nom}: Sotuvda yo‘q!")
        elif miqdor > self.__zaxira:
            print(f"{self.nom}: Faqat {self.__zaxira} dona mavjud.")
        else:
            self.__zaxira -= miqdor
            print(f"{miqdor} dona {self.nom} sotib olindi. Qoldi: {self.__zaxira}")


    def _set_stock(self, yangi_zaxira):
        self.__zaxira = yangi_zaxira


class InventoryManager:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.nom] = product
        print(f"{product.nom} inventarga qo‘shildi.")

    def update_stock(self, product_name, yangi_zaxira):
        if product_name in self.products:
            product = self.products[product_name]
            product._set_stock(yangi_zaxira)
            print(f"{product_name} zaxirasi {yangi_zaxira} taga o‘zgartirildi.")
        else:
            print(f"{product_name} topilmadi.")

    def show_inventory(self):
        print("\n🧾 Inventar ro‘yxati:")
        for p in self.products.values():
            print(p.get_info())


non = Product("Non", 3000, 10)
sut = Product("Sut", 8000, 5)
olma = Product("Olma", 4000, 0)


manager = InventoryManager()
manager.add_product(non)
manager.add_product(sut)
manager.add_product(olma)

manager.show_inventory()

print("\n🛒 Xaridlar:")
non.purchase(3)
olma.purchase(1)
sut.purchase(5)
sut.purchase(1)

manager.show_inventory()

print("\n🔧 Zaxirani yangilash:")
manager.update_stock("Olma", 20)
manager.show_inventory()
