import data
import helpers

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")

    def test_set_route(self):
        print("Função criada para definir a rota")
        # Adicionar em S8
        pass

    def test_select_plan(self):
        print("Função criada para definir o plano de carro")
        # Adicionar em S8
        pass

    def test_fill_phone_number(self):
        print("Função criada para inserir o número de telefone")
        # Adicionar em S8
        pass

    def test_fill_card(self):
        print("Função criada para inserir o número do cartão")
        # Adicionar em S8
        pass

    def test_comment_for_driver(self):
        print("Função criada para inserir um comentário ao motorista")
        # Adicionar em S8
        pass

    def test_order_blanket_and_handkerchiefs(self):
        print("Função criada para pedir cobertor e lençóis")
        # Adicionar em S8
        pass

    def test_order_2_ice_creams(self):
        print("Função criada para pedir sorvetes")
        # Adicionar em S8
        pass

    def test_car_search_model_appears(self):
        print("Função criada para procurar o modelo do carro")
        # Adicionar em S8
        pass

    def test_order_2_ice_creams(self):
        numbers_of_icecreams = 2
        for count in range(numbers_of_icecreams):
            print("Função criada para pedir 2 sorvetes")
            # Adicionar em S8
        pass