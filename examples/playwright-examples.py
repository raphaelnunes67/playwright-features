import base64
from playwright.sync_api import sync_playwright

class PlaywrightExamples():
    def __init__(self):
        self.browser = sync_playwright().start().chromium.launch(headless=False)

    def navigate(self):
        page = self.browser.new_page()
        page.goto("https://google.com")
        print("On page -> " + page.title())
        page.goto("https://bing.com")
        print("On page -> " + page.title())
        print("Refresh")
        page.reload()
        print("Back to google page")
        page.go_back()
        print("Foward to bing page")
        page.go_forward()
        print("On page -> " + page.title())
        page.close()

    def capture_infos(self):
        page = self.browser.new_page()
        page.goto("https://google.com")
        # Preencher campo de pesquisa (Seletor padrão CSS)
        # Mesmo exemplo com Xpath
        # page.locator('xpath=//input[@name="q"]')
        page.locator('[name="q"]').fill("Maps")
        # Capturar informações da página
        print(page.title())
        print(page.inner_html('html'))
        print("valor? -> " + page.locator('[name="q"]').input_value())
        print("oculto? -> " + page.locator('[name="q"]').is_hidden().__str__())
        print("visível? -> " + page.locator('[name="q"]').is_visible().__str__())
        print("disponível? -> " + page.locator('[name="q"]').is_enabled().__str__())
        print("Valor Atributo Aria Label? -> " + page.locator('[name="q"]').get_attribute("aria-label"))
        # close page
        page.close()

    def circle_visible(self):
        page = self.browser.new_page()
        page.goto("http://vanilton.net/web-test/display/")
        #made in Vanilton, Raphael
        print(page.locator('#circle').get_attribute("display"))
        #page.locator('.circle:visible').click()
        #page.locator('.circle >> visible=true').click()
        #page.locator('id=circle-clone').click()
        page.locator("#circle-clone").click()
        page.locator('#refresh-page').click()
        #page.locator('[onclick="AtualizarPagina()"]')
        page.locator("section", has=page.locator(".circle >> visible=true")).click()
        #print(page.locator("section:has(div.circle)").inner_text())
        #print(page.locator('section:has(button#refresh-page)').inner_text())

        sections = page.locator("section")
        for i in range(sections.count()):
            print(sections.nth(i).inner_text())
        #print(sections.all_inner_texts())
        # por índice
        #print(sections.all_inner_texts()[1])
        #sections.nth(1).inner_text()
        #print(sections.locator("h4", has_text="Op").inner_text())
        page.locator('button:has-text("Show Hide Elements"), button:has-text("Exibir Elementos Ocultos")').click()
        print(page.locator('#show-element').inner_text())
        page.locator('button:has-text("Show Hide Elements"), button:has-text("Exibir Elementos Ocultos")').click()
        print(page.locator('#show-element').inner_text())
        page.close()


    def example_xpath(self):
        page = self.browser.new_page()
        page.goto("http://vanilton.net/web-test/display/")
        print("Inner do HTML " + page.locator("xpath=/html").inner_text())
        print("Inner do h4 " + page.locator("xpath=//h4").all_inner_texts().__str__())
        print("Inner do parent h4 " + page.locator("xpath=//h4/..").all_inner_texts().__str__())
        print("Inner de @style elements " + page.locator("xpath=//@style").all_inner_texts().__str__())
        page.close()

    def example_xpath_predicate(self):
        page = self.browser.new_page()
        page.goto("http://vanilton.net/web-test/display/")
        print("SECTION 1", page.locator("xpath=//section[1]").inner_text())
        print("SECTION LAST", page.locator("xpath=//section[last()]").inner_text())
        print("SECTION LAST -1 ", page.locator("xpath=//section[last()-1]").inner_text())
        print("CLASS ROUNDED", page.locator("xpath=//div[@class='rounded']").inner_text())
        print("SECTION / ELEMENTS > 3", page.locator("xpath=//section/*[position() >3]").all_inner_texts())
        print("ONCLICK FUNCTION", page.locator("xpath=//*[@onclick]").inner_text())
        page.close()


    def example_xpath_functions(self):
        page = self.browser.new_page()
        page.set_default_timeout(5000)
        page.goto("http://vanilton.net/web-test/display/")
        print(page.locator("xpath=//button[contains(.,'Exibir')]").all_inner_texts())
        print(page.locator("xpath=//button[contains(.,'Exibir')] | //button[contains(.,'Hide')]").all_inner_texts())
        print(page.locator("xpath=//button[text()='Show Hide Elements']").all_inner_texts())
        print(page.locator("xpath=//button[@id and @onclick]").inner_text())
        print(page.locator('xpath=//div[contains(@id, "clone")]').get_attribute("id"))
        page.close()


    def example_edit_person(self):
        page = self.browser.new_page()
        page.set_default_timeout(5000)
        page.goto("https://vanilton18.github.io/crud-local-storage-angular/")
        page.locator('id=nome').fill("Vanilton de Souza Freire Pinheiro")
        page.locator('[placeholder="Digite um email"]').fill("vanilton18@gmail.com")
        url_foto = "https://i.pinimg.com/originals/e4/34/2a/e4342a4e0e968344b75cf50cf1936c09.jpg"
        page.locator('[name=photo]').fill(url_foto)
        page.locator('text=Save').click()
        print(page.locator('xpath=//div[@class="card-block" and contains(.,"Vanilton")]').inner_text())
        # com xpath
        page.locator('xpath=//div[@class="card-block" and contains(.,"Vanilton")]//button[contains(.,"Editar")]').click()
        # com css
        #page.locator("css=div.card:has-text('Vanilton') >> css=button >> text=Edit").click()
        page.locator('id=nome').fill("Vanilton de S.F. Pinheiro")
        page.locator('[placeholder="Digite um email"]').fill("vanilton18@hotmail.com")
        page.locator('text=Save').click()
        print(page.locator('xpath=//div[@class="card-block" and contains(.,"Vanilton")]').inner_text())
        #print(page.locator('id=toast-container', has_text='Edição efetuada com sucesso!').is_visible())
        print(page.locator('[aria-label="Edição efetuada com sucesso!"]').is_visible())
        page.close()

    def handle_dialog(self, dialog):
        print(dialog.message)

    def example_remove_registered_person(self):
        page = self.browser.new_page()
        page.set_default_timeout(5000)
        page.goto("https://vanilton18.github.io/crud-local-storage-angular/")
        page.locator('id=nome').fill("Vanilton de Souza Freire Pinheiro")
        page.locator('[placeholder="Digite um email"]').fill("vanilton18@gmail.com")
        url_foto = "https://i.pinimg.com/originals/e4/34/2a/e4342a4e0e968344b75cf50cf1936c09.jpg"
        page.locator('[name=photo]').fill(url_foto)
        page.locator('text=Save').click()
        print(page.locator('xpath=//div[@class="card-block" and contains(.,"Vanilton")]').inner_text())
        page.locator('xpath=//div[@class="card-block" and contains(.,"Vanilton")]//button[contains(.,"Remover")]').scroll_into_view_if_needed()
        remove = page.locator("css=div.card:has-text('Vanilton') >> css=button >> text=Remover")
        page.on("dialog", lambda dialog: dialog.accept()) #Evento de captura do dialog
        page.on("dialog", self.handle_dialog)
        remove.click()
        print(page.locator("xpath=//div[@class='row']").inner_text() == '')
        page.close()

    def example_shadow_dom_acess(self):
        page = self.browser.new_page()
        page.set_default_timeout(5000)
        page.goto("http://vanilton.net/web-test/shadow-dom/")
        #print(page.locator('xpath=//fancy-tabs').locator('#nome').get_attribute("placeholder"))
        print(page.locator(':light(#nome)').get_attribute("placeholder"))
        page.close()

    def example_layout_locator(self):
        page = self.browser.new_page()
        page.set_default_timeout(5000)
        page.goto("http://vanilton.net/web-test/shadow-dom/")
        print(page.locator("button:right-of(:text('Tab 2'))").first.inner_text())
        print(page.locator("button:left-of(:text('Tab 2'))").first.inner_text())
        #print(page.locator("button:left-of(:text('Tab 2'))").inner_text())
        #print(page.locator("button:right-of(:text('Tab 2'))").inner_text())
        print(page.locator(":above(:text('Tab 2'))").count())
        print(page.locator(":below(:text('Tab 2'))").count())
        print(page.locator("button:near(:text('Tab 2'))").all_inner_texts())
        page.close()

    def example_calculate_sqrt(self):
        page = self.browser.new_page()
        page.set_default_timeout(5000)
        page.goto("http://vanilton.net/calculatorSoapPHP/")
        #page.locator('input[name=num1] >> nth=1').fill("4")
        #page.locator('text="Resultado" >> nth=1').click()
        page.locator('[name="num1"] >> nth=1').fill('10')
        page.locator('text="Resultado" >> nth=-1').click()
        print(page.locator('html').inner_text())
        page.close()

    def example_calculate_sum(self):
        page = self.browser.new_page()
        page.set_default_timeout(5000)
        page.goto("http://vanilton.net/calculatorSoapPHP/")
        page.locator("input >> nth=0").fill('300')
        page.locator("input >> nth=1").fill('100')
        print(page.locator("input >> nth=0").input_value())
        page.locator("input[value='Resultado'] >> nth=0").click()
        print(page.locator('html').inner_text())
        page.close()

    def example_calculate_divided(self):
        page = self.browser.new_page()
        page.set_default_timeout(5000)
        page.goto("http://vanilton.net/calculatorSoapPHP/")
        page.locator("input >> nth=0").fill('300')
        page.select_option('xpath=//select/option[contains(@value,"sum")]/..', value="div")
        page.locator("input >> nth=1").fill('100')
        print(page.locator("input >> nth=0").input_value())
        page.locator("input[value='Resultado'] >> nth=0").click()
        print(page.locator('html').inner_text())
        page.close()

    def example_calculate_product(self):
        page = self.browser.new_page()
        page.set_default_timeout(5000)
        page.goto("http://vanilton.net/calculatorSoapPHP/")
        page.locator("input >> nth=0").fill('300')
        page.locator("input >> nth=0").fill('500')
        select = page.locator('select:has-text("*")')
        select.select_option(label="*")
        page.locator("input >> nth=1").fill('100')
        print(page.locator("input >> nth=0").input_value())
        page.locator("input[value='Resultado'] >> nth=0").click()
        print(page.locator('html').inner_text())
        page.close()

    def example_calculate_subtraction(self):
        page = self.browser.new_page()
        page.set_default_timeout(5000)
        page.goto("http://vanilton.net/calculatorSoapPHP/")
        page.locator("input >> nth=0").fill('300')
        page.select_option('select:has-text("*")', index=1)
        page.locator("input >> nth=1").fill('100')
        print(page.locator("input >> nth=0").input_value())
        page.locator("input[value='Resultado'] >> nth=0").click()
        print(page.locator('html').inner_text())
        page.close()

    def example_calculator(self):
        page = self.browser.new_page()
        page.set_default_timeout(5000)
        page.goto("http://vanilton.net/calculatorSoapPHP/")
        page.locator("input >> nth=0").type("2", delay=1000)
        select = page.locator('select:has-text("*")')
        select.select_option(label="*")
        page.locator("input >> nth=1").type("4", delay=1000)
        page.locator("input[value='Resultado'] >> nth=0").click()
        #resultado = page.locator('body').inner_text().split('\n')[0]
        resultado = page.evaluate('x = document.getElementsByTagName("body")[0]; x.firstChild.textContent')
        print(resultado)
        # Raiz Quadrada
        page.go_back()
        page.reload()
        page.locator('[name="num1"] >> nth=1').type("4", delay=1000)
        page.locator('text="Resultado" >> nth=-1').click()
        #resultado = page.locator('body').inner_text().split('\n')[0]
        resultado = page.evaluate('x = document.getElementsByTagName("body")[0]; x.firstChild.textContent')
        print(resultado)
        page.go_back()
        page.reload()
        # Cosseno
        select = page.locator('select:has-text("Raiz")')
        select.select_option(label="Coseno")
        page.locator('[name="num1"] >> nth=1').type("5", delay=1000)
        page.locator('text="Resultado" >> nth=-1').click()
        #resultado = page.locator('body').inner_text().split('\n')[0]
        resultado = page.evaluate('x = document.getElementsByTagName("body")[0]; x.firstChild.textContent')
        print(resultado)
        page.close()

    def example_evaluate_screen_size(self):
        page = self.browser.new_page()
        page.set_default_timeout(5000)
        page.goto("http://vanilton.net/web-test/promise/")
        # Cria o objeto window
        object_handle = page.evaluate_handle('window')
        print(object_handle.json_value())
        # Passando por parâmetro um handle e recuperando seu innerHTML
        body_handle = page.evaluate_handle('document.body')
        body_text = page.evaluate("body => body.innerHTML", body_handle)
        print(body_text)
        # Tamanho da tela
        width = page.evaluate_handle('window.screen.width')
        height = page.evaluate_handle('window.screen.height')
        print("Largura: {} - Altura: {}".format(width, height))
        # Encerra a referência ao elemento
        body_handle.dispose()
        object_handle.dispose()
        page.close()

    def exemplo_element_handle(self):
        page = self.browser.new_page()
        page.goto("http://vanilton.net/blog")
        href_element = page.query_selector("a")
        print(href_element.inner_text())
        page.close()

    def example_keyboard(self):
        page = self.browser.new_page()
        page.goto("https://google.com")
        busca = page.locator('[name="q"]')
        busca.focus()
        page.keyboard.type("Hello World!", delay=500)
        page.keyboard.press("ArrowLeft")
        page.keyboard.down("Shift")  # down (segura a tecla)
        for i in range(6):
            page.keyboard.press("ArrowLeft", delay=1000)
        page.keyboard.up("Shift")  # up (solta a tecla)
        page.keyboard.press("Backspace")
        print(busca.input_value())
        page.close()

    def example_keyboard(self):
        page = self.browser.new_page()
        page.goto("https://keycode.info")
        page.keyboard.type('Meta+a')
        print(page.locator('div.item-event').inner_text())
        page.screenshot(path='image/meu_primeiro_screenshot2.png', full_page=True)
        page.locator('div.item-event').screenshot(path='image/card-event2.png')
        page.close()
    def print_request_sent(self, request):
        print("Request sent: " + request.url)

    def print_request_finished(self, request):
        print("Request finished: " + request.url)

    def print_request_response(self, request):
        print("Request response: " + request.url)

    # Execute essa função e observe o console da IDE
    def test_wait_add_remove_event_listener(self):
        page = self.browser.new_page()
        page.on("request", self.print_request_sent)
        page.on("response", self.print_request_response)
        page.on("requestfinished", self.print_request_finished)
        page.remove_listener("requestfinished", self.print_request_finished)
        page.goto("https://ge.globo.com")
        page.goto("https://wikipedia.org")
        page.close()

    def example_evento_expect_request(self):
        page = self.browser.new_page()
        #with page.expect_request("**/*teste*.png") as first:
        with page.expect_request("**teste_agil-520x389.png") as first:
            page.goto("http://vanilton.net/blog")
        print(first.is_done())
        print(first.value.headers)
        print(first.value.url)
        print(first.value.response())
        page.close()

    def example_iframe(self):
        page = self.browser.new_page()
        page.goto("http://vanilton.net/web-test/iframe/")
        frame_element = page.frame_locator('[name=iframe_artigos]')
        print(frame_element.locator('title').inner_text())
        page.locator('text=Como ser um facilitador?').click()
        frame_element.locator('[id=page]').wait_for(timeout=10000)
        print(frame_element.locator('title').inner_text())
        page.close()

    def example_check_and_radio_buttons(self):
        page = self.browser.new_page()
        page.goto("http://vanilton.net/web-test/input-types/")
        page.locator('id=M').check()
        print(page.locator('id=output').inner_text().__contains__('M') is True)
        page.locator('id=Bike').check()
        page.locator('id=Moto').check()
        print(page.locator('id=Moto').is_checked())
        print(page.locator('id=Bike').is_checked())
        print(page.locator('id=Barco').is_checked())
        print(page.locator('id=output-check').inner_text().__contains__('Bike' and 'Moto') is True)
        screen = page.screenshot()
        result = base64.b64encode(screen).decode()
        print(result)
        page.close()

    def example_save_images(self):
        page = self.browser.new_page()
        page.goto('http://lojafake.vanilton.net')
        page.locator('img').first.wait_for(state='visible')
        page.screenshot(path='image/loja-fake.png', full_page=True)
        images = page.locator('img')
        for i in range(images.count()):
            nome = images.nth(i).get_attribute('name')
            images.nth(i).screenshot(path=f'images/{nome}.png')
        page.close()

    def example_store_fake(self):
        page = self.browser.new_page()
        page.goto("http://lojafake.vanilton.net/")
        page.locator("div:has-text(\"Usuário\")").nth(4).click()
        page.locator("#mat-input-0").fill("admin")
        page.locator("#mat-input-1").fill("1234")
        page.locator("button:has-text(\"Login\")").click()
        page.locator("text=Minhas Listas").click()
        page.wait_for_url("http://lojafake.vanilton.net/#/drag-drop")
        page.locator("text=Filmes").click()
        page.close()

    def example_drag_drop_html5(self):
        page = self.browser.new_page()
        page.goto("http://vanilton.net/web-test/drag-drop/")
        page.drag_and_drop("id=drag1", 'id=div2')
        print(page.locator("[id='content1']").inner_text())
        page.drag_and_drop("id=drag1", "id=div1")
        print(page.locator("[id='content2']").inner_text())
        page.close()


if __name__ == '__main__':
   pw = PlaywrightExamples()
   pw.example_calculator()
