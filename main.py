import gspread
from oauth2client.service_account import ServiceAccountCredentials
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label  # Label sınıfını ekledik
from kivy.uix.button import Button


    
   


class Siparis_Kaydetme(App):
    def build(self):
        self.text_input = TextInput()
        self.result_label = Label()
        self.save_button = Button(text="Kaydet")
        self.save_button.bind(on_press=self.process_text)
        
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.text_input)
        layout.add_widget(self.save_button)
        layout.add_widget(self.result_label)
        
        return layout

    def process_text(self, instance):
        input_text = self.text_input.text
        
        # Satırlara bölmek için '\n' karakterini kullanabilirsiniz
        lines = input_text.split('\n')
        sube_kodu='205'
        en='10'
        boy='15'
        yukseklik='10'
        miktar='1'
        gram ='800'
        gturu='2'
        ucrettutu='6'
        ekhizmet=''
        kdv ='8'
        sipno=''
        cıkısno=''
        satıcı=''
        hattar=''
        fattar=''
        bos=''

        if len(lines) >= 6:
            isim_soyisim = lines[0]
            adres_bilgisi = lines[1]
            il =lines[2]
            ilce = lines[3]
            telefon = lines[4]
            ucret = lines[5]
            urun_bilgisi = '\n'.join(lines[7:])
            
            # Sonuçları etiket üzerinde gösterme
            result_text = f"İsim Soyisim: {isim_soyisim}\nAdres Bilgisi: {adres_bilgisi}\nTelefon: {telefon}\nİl :{il}\nİlçe : {ilce}\nÜcret : {ucret}\nÜrün Bilgisi:\n{urun_bilgisi}"
            self.result_label.text = result_text
            scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
                    "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
            credentials = ServiceAccountCredentials.from_json_keyfile_name("veri-cekme.json", scope)

    # Kimlik doğrulama yap
            gc = gspread.authorize(credentials)

    # Hedef Google Tablosu belgesini aç
            worksheet = gc.open("telefon").worksheet("Sayfa1")
            last_row = len(worksheet.col_values(1)) + 1

            data_to_insert = [isim_soyisim, ilce, il, adres_bilgisi,telefon,sube_kodu,bos,ucret,urun_bilgisi,miktar,gram,gturu,ucrettutu,ekhizmet,kdv,sipno,cıkısno,satıcı,hattar,fattar,en,boy,yukseklik]
            worksheet.insert_row(data_to_insert, last_row)
            
           
        else:
            self.result_label.text = "Lütfen girdiyi doğru bir şekilde ayırın."

if __name__ == '__main__':
    Siparis_Kaydetme().run()







# Kimlik doğrulama bilgileri JSON dosyası



def process_text(self, instance):
    input_text = self.text_input.text

    # Satırlara bölmek için '\n' karakterini kullanabilirsiniz
    lines = input_text.split('\n')

    if len(lines) >= 3:
        isim_soyisim = lines[0]
        adres_bilgisi = lines[1]
        il = lines[2]
        ilce = lines[3]
        telefon = lines[4]
        ucret = lines[5]
        urun_bilgisi = '\n'.join(lines[6:])

        # Sonuçları etiket üzerinde gösterme
        result_text = f"İsim Soyisim: {isim_soyisim}\nAdres Bilgisi: {adres_bilgisi}\nTelefon: {telefon}\nİl: {il}\nİlçe: {ilce}\nÜcret: {ucret}\nÜrün Bilgisi:\n{urun_bilgisi}"
        self.result_label.text = result_text

        # Verileri Google Tablosuna ekleyin
        
        

    else:
        self.result_label.text = "Lütfen girdiyi doğru bir şekilde ayırın."
