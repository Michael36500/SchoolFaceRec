import face_recognition
import cv2
from imageio import volread
import numpy as np
# import def_load as load
import random as rn
import time

Start = time.time()

import face_recognition
import cv2
import numpy as np
from scipy.misc import face

def img(where):
    global total_faces
    global act_face
    act_face = act_face + 1
    print("picture loaded ", where, "\t\t\t\t", act_face, "of", total_faces)
    image = face_recognition.load_image_file(where)
    # print(image)
    
    face_encoding = face_recognition.face_encodings(image)
    if str(face_encoding) == "[]":
        print("NO FINDABLE FACES!!!")
    # face_encoding = face_encoding[0]
    # print(face_encoding)

    return face_encoding [0]

def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
print("GO!")
for a in range(10):
    print("trying", a)
    video_capture = cv2.VideoCapture(a, cv2.CAP_DSHOW)
    ret, frame = video_capture.read()
    print(ret)
    if ret == True:
        break
    else:
        video_capture.release()
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
total_faces = 452
act_face = 0
# video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)




print("video captured")
# print(video_capture)

# Load a sample picture and learn how to recognize it.





















AbrahamovaTv = img("faces/AbrahamovaTv.jpg")
Adamikova2AjRuD = img("faces/Adamikova2AjRuD.jpg")
BednarikovaMaITV = img("faces/BednarikovaMaITV.jpg")
BerankovaAjFr = img("faces/BerankovaAjFr.jpg")
BraunerChBi = img("faces/BraunerChBi.jpg")
CastellarSp = img("faces/CastellarSp.jpg")
CechovaAj = img("faces/CechovaAj.jpg")
ChromaTvZ = img("faces/ChromaTvZ.jpg")
DanielTvZ = img("faces/DanielTvZ.jpg")
DohnalovaCjHv = img("faces/DohnalovaCjHv.jpg")
DostalovaTv = img("faces/DostalovaTv.jpg")
DubovaNeCj = img("faces/DubovaNeCj.jpg")
DvorskyAjD = img("faces/DvorskyAjD.jpg")
FaberovaAjRu = img("faces/FaberovaAjRu.jpg")
FerencMaFy = img("faces/FerencMaFy.jpg")
FukaCjNe = img("faces/FukaCjNe.jpg")
GlosCjD = img("faces/GlosCjD.jpg")
HajduMaAj = img("faces/HajduMaAj.jpg")
HajekBiCh = img("faces/HajekBiCh.jpg")
HamrikovaMaCh = img("faces/HamrikovaMaCh.jpg")
HavranovaAj = img("faces/HavranovaAj.jpg")
HermanovaCjHvRu = img("faces/HermanovaCjHvRu.jpg")
HorvathSp = img("faces/HorvathSp.jpg")
HubackovaCjD = img("faces/HubackovaCjD.jpg")
IA4BerkovaAnna = img("faces/IA4BerkovaAnna.png")
IA4BilikovaAlzbeta = img("faces/IA4BilikovaAlzbeta.png")
IA4BrstakovaJulie = img("faces/IA4BrstakovaJulie.png")
IA4BubenickovaAneta = img("faces/IA4BubenickovaAneta.png")
IA4BuczkovaBarbora = img("faces/IA4BuczkovaBarbora.png")
IA4ChmelikLukas = img("faces/IA4ChmelikLukas.png")
IA4DankovaKarolina = img("faces/IA4DankovaKarolina.png")
IA4GalnorJakub = img("faces/IA4GalnorJakub.png")
IA4GjurgjealaKaona = img("faces/IA4GjurgjealaKaona.png")
IA4HalovaBarbora = img("faces/IA4HalovaBarbora.png")
IA4HimrMatej = img("faces/IA4HimrMatej.png")
IA4HodurovaKEliska = img("faces/IA4HodurovaKEliska.png")
IA4JanalikTomas = img("faces/IA4JanalikTomas.png")
IA4KostkaJan = img("faces/IA4KostkaJan.png")
IA4KoukalFrantisek = img("faces/IA4KoukalFrantisek.png")
IA4KrejciMatyas = img("faces/IA4KrejciMatyas.png")
IA4LipkovaValerie = img("faces/IA4LipkovaValerie.png")
IA4LosikLeonard = img("faces/IA4LosikLeonard.png")
IA4MachovaDagmar = img("faces/IA4MachovaDagmar.png")
IA4PolednaJan = img("faces/IA4PolednaJan.png")
IA4StavarskaLucie = img("faces/IA4StavarskaLucie.png")
IA4StechovaBarbora = img("faces/IA4StechovaBarbora.png")
IA4StejskalovaLinda = img("faces/IA4StejskalovaLinda.png")
IA4VaculikPetr = img("faces/IA4VaculikPetr.png")
IA4WestphalDavid = img("faces/IA4WestphalDavid.png")
IA6BaresovaKlara = img("faces/IA6BaresovaKlara.png")
IA6BelohlavkovaMarie = img("faces/IA6BelohlavkovaMarie.png")
IA6CapalovaKarolina = img("faces/IA6CapalovaKarolina.png")
IA6FedorcoMarian = img("faces/IA6FedorcoMarian.png")
IA6FilousovaLena = img("faces/IA6FilousovaLena.png")
IA6HorklovaKatka = img("faces/IA6HorklovaKatka.png")
IA6KlosovaMarie = img("faces/IA6KlosovaMarie.png")
IA6KvapilMichael = img("faces/IA6KvapilMichael.png")
IA6LukasovaAdela = img("faces/IA6LukasovaAdela.png")
IA6MachStepan = img("faces/IA6MachStepan.png")
IA6MaslikovaTereza = img("faces/IA6MaslikovaTereza.png")
IA6NavratilJachym = img("faces/IA6NavratilJachym.png")
IA6PridalMatej = img("faces/IA6PridalMatej.png")
IA6PtackovaEliska = img("faces/IA6PtackovaEliska.png")
IA6SimakStepan = img("faces/IA6SimakStepan.png")
IA6SouckovaSara = img("faces/IA6SouckovaSara.png")
IA6SouckovaZdenka = img("faces/IA6SouckovaZdenka.png")
IA6SouskovaEliska = img("faces/IA6SouskovaEliska.png")
IA6StarostovaTereza = img("faces/IA6StarostovaTereza.png")
IA6StybnarMarek = img("faces/IA6StybnarMarek.png")
IA6SvobodaDavid = img("faces/IA6SvobodaDavid.png")
IA6UherJan = img("faces/IA6UherJan.png")
IA6ValekDan = img("faces/IA6ValekDan.png")
IA6VrajovaJana = img("faces/IA6VrajovaJana.png")
IA6VyroubalRadek = img("faces/IA6VyroubalRadek.png")
IA6WittmannovaJAnna = img("faces/IA6WittmannovaJAnna.png")
IA6ZelenkovaTereza = img("faces/IA6ZelenkovaTereza.png")
IA6ZemberovaDaniela = img("faces/IA6ZemberovaDaniela.png")
IA8AuxtovaLinda = img("faces/IA8AuxtovaLinda.png")
IA8BartosJan = img("faces/IA8BartosJan.png")
IA8BenesovaJohana = img("faces/IA8BenesovaJohana.png")
IA8BouchalovaKveta = img("faces/IA8BouchalovaKveta.png")
IA8ChmelovaVendula = img("faces/IA8ChmelovaVendula.png")
IA8CisarVojtech = img("faces/IA8CisarVojtech.png")
IA8DostalJakub = img("faces/IA8DostalJakub.png")
IA8FilousovaAlzbeta = img("faces/IA8FilousovaAlzbeta.png")
IA8GajdusekMiroslav = img("faces/IA8GajdusekMiroslav.png")
IA8GogolJMatyas = img("faces/IA8GogolJMatyas.png")
IA8GrassovaEla = img("faces/IA8GrassovaEla.png")
IA8HalatovaVeronika = img("faces/IA8HalatovaVeronika.png")
IA8HandlovaKaterina = img("faces/IA8HandlovaKaterina.png")
IA8HarnosovaAlzbeta = img("faces/IA8HarnosovaAlzbeta.png")
IA8HulikovaAmelie = img("faces/IA8HulikovaAmelie.png")
IA8IlleovaAdela = img("faces/IA8IlleovaAdela.png")
IA8JensDavid = img("faces/IA8JensDavid.png")
IA8KmentovaMarie = img("faces/IA8KmentovaMarie.png")
IA8KornhonTomas = img("faces/IA8KornhonTomas.png")
IA8KropacDavid = img("faces/IA8KropacDavid.png")
IA8LonicekMartin = img("faces/IA8LonicekMartin.png")
IA8MaslikovaKarolina = img("faces/IA8MaslikovaKarolina.png")
IA8MohylovaLaura = img("faces/IA8MohylovaLaura.png")
IA8MuchovaJohana = img("faces/IA8MuchovaJohana.png")
IA8NavratilDaniel = img("faces/IA8NavratilDaniel.png")
IA8ProchazkaJan = img("faces/IA8ProchazkaJan.png")
IA8StefanuttovaAmalie = img("faces/IA8StefanuttovaAmalie.png")
IA8SterbovaSDana = img("faces/IA8SterbovaSDana.png")
IA8TichyMaxmilian = img("faces/IA8TichyMaxmilian.png")
IA8ZdrazilovaAKarolina = img("faces/IA8ZdrazilovaAKarolina.png")
IB4ApplovaPavlina = img("faces/IB4ApplovaPavlina.png")
IB4BacikZeyner = img("faces/IB4BacikZeyner.png")
IB4HavlikMatyas = img("faces/IB4HavlikMatyas.png")
IB4HrancovaMarketa = img("faces/IB4HrancovaMarketa.png")
IB4HrnkovaGita = img("faces/IB4HrnkovaGita.png")
IB4JarosMichael = img("faces/IB4JarosMichael.png")
IB4KalabisovaAnna = img("faces/IB4KalabisovaAnna.png")
IB4KejklickovaTereza = img("faces/IB4KejklickovaTereza.png")
IB4MachVKrystof = img("faces/IB4MachVKrystof.png")
IB4MadrovaAdriana = img("faces/IB4MadrovaAdriana.png")
IB4MalaLenka = img("faces/IB4MalaLenka.png")
IB4MykhailetsVadim = img("faces/IB4MykhailetsVadim.png")
IB4PopelkaStepan = img("faces/IB4PopelkaStepan.png")
IB4PospisilovaZuzana = img("faces/IB4PospisilovaZuzana.png")
IB4PrincDaniel = img("faces/IB4PrincDaniel.png")
IB4SalamonJan = img("faces/IB4SalamonJan.png")
IB4SittekJakub = img("faces/IB4SittekJakub.png")
IB4SkladanyLukas = img("faces/IB4SkladanyLukas.png")
IB4SkrontovaEliska = img("faces/IB4SkrontovaEliska.png")
IB4SkurkovaAdela = img("faces/IB4SkurkovaAdela.png")
IB4SpevakovaEva = img("faces/IB4SpevakovaEva.png")
IB4StojakovaLucie = img("faces/IB4StojakovaLucie.png")
IB4StolfovaNatalie = img("faces/IB4StolfovaNatalie.png")
IB4TajovskaNikola = img("faces/IB4TajovskaNikola.png")
IB4VejmolovaKarolina = img("faces/IB4VejmolovaKarolina.png")
IB6BrodaJakub = img("faces/IB6BrodaJakub.png")
IB6CventanovaKaterina = img("faces/IB6CventanovaKaterina.png")
IB6FisaraDavid = img("faces/IB6FisaraDavid.png")
IB6KonecnaLucie = img("faces/IB6KonecnaLucie.png")
IB6KonecnyVit = img("faces/IB6KonecnyVit.png")
IB6KriegovaPavlina = img("faces/IB6KriegovaPavlina.png")
IB6KrizAntonin = img("faces/IB6KrizAntonin.png")
IB6KubelkaErik = img("faces/IB6KubelkaErik.png")
IB6LejskovaAdela = img("faces/IB6LejskovaAdela.png")
IB6LosikovaLada = img("faces/IB6LosikovaLada.png")
IB6MacickovaJana = img("faces/IB6MacickovaJana.png")
IB6MiksikovaNatalie = img("faces/IB6MiksikovaNatalie.png")
IB6MikulovaBerenika = img("faces/IB6MikulovaBerenika.png")
IB6NajerMarek = img("faces/IB6NajerMarek.png")
IB6NepovimovaLucie = img("faces/IB6NepovimovaLucie.png")
IB6NovotnyOndrej = img("faces/IB6NovotnyOndrej.png")
IB6PribylVojtech = img("faces/IB6PribylVojtech.png")
IB6RobertsonTomas = img("faces/IB6RobertsonTomas.png")
IB6RybaFrantisek = img("faces/IB6RybaFrantisek.png")
IB6SedajovaSarka = img("faces/IB6SedajovaSarka.png")
IB6SobekTomas = img("faces/IB6SobekTomas.png")
IB6SohnelDavid = img("faces/IB6SohnelDavid.png")
IB6StefanovaEma = img("faces/IB6StefanovaEma.png")
IB6StrnadelMichael = img("faces/IB6StrnadelMichael.png")
IB6SyrovatkovaEliska = img("faces/IB6SyrovatkovaEliska.png")
IB6UrbamkovaAnezka = img("faces/IB6UrbamkovaAnezka.png")
IB6UtikalovaLLeontyna = img("faces/IB6UtikalovaLLeontyna.png")
IB6VohankovaKlara = img("faces/IB6VohankovaKlara.png")
IB6ZborilovaSara = img("faces/IB6ZborilovaSara.png")
IB8BrundaMikulas = img("faces/IB8BrundaMikulas.png")
IB8BurdaJan = img("faces/IB8BurdaJan.png")
IB8ChrasteckyJan = img("faces/IB8ChrasteckyJan.png")
IB8DoubalovaJarmila = img("faces/IB8DoubalovaJarmila.png")
IB8FischerOndrej = img("faces/IB8FischerOndrej.png")
IB8GastaPetr = img("faces/IB8GastaPetr.png")
IB8IloemezueBeaAdachi = img("faces/IB8IloemezueBeaAdachi.png")
IB8KlimcakRichard = img("faces/IB8KlimcakRichard.png")
IB8KonecnaElla = img("faces/IB8KonecnaElla.png")
IB8KubickovaSofire = img("faces/IB8KubickovaSofire.png")
IB8KubikJachym = img("faces/IB8KubikJachym.png")
IB8LacovaKristina = img("faces/IB8LacovaKristina.png")
IB8LinekOndrej = img("faces/IB8LinekOndrej.png")
IB8MachacovaEdita = img("faces/IB8MachacovaEdita.png")
IB8MorbicrovaAdela = img("faces/IB8MorbicrovaAdela.png")
IB8NgoTuongVan = img("faces/IB8NgoTuongVan.png")
IB8OndrouskovaTereza = img("faces/IB8OndrouskovaTereza.png")
IB8OpavskyVit = img("faces/IB8OpavskyVit.png")
IB8PeterovaMichaela = img("faces/IB8PeterovaMichaela.png")
IB8PiechDaniel = img("faces/IB8PiechDaniel.png")
IB8RaabovaIva = img("faces/IB8RaabovaIva.png")
IB8StoppenovaJulie = img("faces/IB8StoppenovaJulie.png")
IB8TisovskyMikulas = img("faces/IB8TisovskyMikulas.png")
IB8UtikalovaNJustyna = img("faces/IB8UtikalovaNJustyna.png")
IB8VelickyVaclav = img("faces/IB8VelickyVaclav.png")
IB8VodickovaKristyna = img("faces/IB8VodickovaKristyna.png")
IB8ZavadilTomas = img("faces/IB8ZavadilTomas.png")
IB8ZdarilDaniel = img("faces/IB8ZdarilDaniel.png")
IIA4AndršJan = img("faces/IIA4AndršJan.png")
IIA4BiskupovaSimona = img("faces/IIA4BiskupovaSimona.png")
IIA4BlumaJan = img("faces/IIA4BlumaJan.png")
IIA4ChodurkovaAnna = img("faces/IIA4ChodurkovaAnna.png")
IIA4ChytilovaKarolina = img("faces/IIA4ChytilovaKarolina.png")
IIA4DrahotuskaAmalie = img("faces/IIA4DrahotuskaAmalie.png")
IIA4DvorskaVeronika = img("faces/IIA4DvorskaVeronika.png")
IIA4FrancakovaKarla = img("faces/IIA4FrancakovaKarla.png")
IIA4FrkalFIlip = img("faces/IIA4FrkalFIlip.png")
IIA4FrumarovaAdela = img("faces/IIA4FrumarovaAdela.png")
IIA4HolikovaNatalie = img("faces/IIA4HolikovaNatalie.png")
IIA4HrabalovaKlara = img("faces/IIA4HrabalovaKlara.png")
IIA4HrbackovaKristyna = img("faces/IIA4HrbackovaKristyna.png")
IIA4HrbatovaEva = img("faces/IIA4HrbatovaEva.png")
IIA4HunovaDenisa = img("faces/IIA4HunovaDenisa.png")
IIA4JancikovaLucie = img("faces/IIA4JancikovaLucie.png")
IIA4JanecekJakub = img("faces/IIA4JanecekJakub.png")
IIA4KudybBenjamin = img("faces/IIA4KudybBenjamin.png")
IIA4LekešMatyas = img("faces/IIA4LekešMatyas.png")
IIA4MatejJiri = img("faces/IIA4MatejJiri.png")
IIA4MikulkaPetr = img("faces/IIA4MikulkaPetr.png")
IIA4NemecJakub = img("faces/IIA4NemecJakub.png")
IIA4PekarJakub = img("faces/IIA4PekarJakub.png")
IIA4SaladakTobias = img("faces/IIA4SaladakTobias.png")
IIA4SevernakovaVeronika = img("faces/IIA4SevernakovaVeronika.png")
IIA4SmetakMarek = img("faces/IIA4SmetakMarek.png")
IIA4ZymovaAneta = img("faces/IIA4ZymovaAneta.png")
IIA6BazgerovaEllen = img("faces/IIA6BazgerovaEllen.png")
IIA6DolezalovaElla = img("faces/IIA6DolezalovaElla.png")
IIA6DracJan = img("faces/IIA6DracJan.png")
IIA6DreslerVaclva = img("faces/IIA6DreslerVaclva.png")
IIA6FilipovaKarolina = img("faces/IIA6FilipovaKarolina.png")
IIA6FrybortovaElisa = img("faces/IIA6FrybortovaElisa.png")
IIA6HamalovaAlzbeta = img("faces/IIA6HamalovaAlzbeta.png")
IIA6HomolacovaDarina = img("faces/IIA6HomolacovaDarina.png")
IIA6HorakovaEma = img("faces/IIA6HorakovaEma.png")
IIA6HorvathMatus = img("faces/IIA6HorvathMatus.png")
IIA6KolousekMarek = img("faces/IIA6KolousekMarek.png")
IIA6KysucanovaMilena = img("faces/IIA6KysucanovaMilena.png")
IIA6LerchStepan = img("faces/IIA6LerchStepan.png")
IIA6MaskovaEEmma = img("faces/IIA6MaskovaEEmma.png")
IIA6PavelkovaZuzana = img("faces/IIA6PavelkovaZuzana.png")
IIA6PilchovaZuzana = img("faces/IIA6PilchovaZuzana.png")
IIA6PlesnikAdam = img("faces/IIA6PlesnikAdam.png")
IIA6SvetlikovaEma = img("faces/IIA6SvetlikovaEma.png")
IIA6TranNguyenHongMai = img("faces/IIA6TranNguyenHongMai.png")
IIA6VaclavikovaNicol = img("faces/IIA6VaclavikovaNicol.png")
IIA6VitkovaAneta = img("faces/IIA6VitkovaAneta.png")
IIA6VlkovaEliska = img("faces/IIA6VlkovaEliska.png")
IIA6VrtalovaPetra = img("faces/IIA6VrtalovaPetra.png")
IIA6WiedermannovaEla = img("faces/IIA6WiedermannovaEla.png")
IIA6ZatloukalovaNela = img("faces/IIA6ZatloukalovaNela.png")
IIA6ZeitlerSamuel = img("faces/IIA6ZeitlerSamuel.png")
IIA6ZidkovaBarbora = img("faces/IIA6ZidkovaBarbora.png")
IIA8BalnerJakub = img("faces/IIA8BalnerJakub.png")
IIA8CablikovaAnna = img("faces/IIA8CablikovaAnna.png")
IIA8CernaStella = img("faces/IIA8CernaStella.png")
IIA8CoufalovaBerenika = img("faces/IIA8CoufalovaBerenika.png")
IIA8DupalovaMichaela = img("faces/IIA8DupalovaMichaela.png")
IIA8HajekKrystof = img("faces/IIA8HajekKrystof.png")
IIA8HamplJonas = img("faces/IIA8HamplJonas.png")
IIA8HebelkaEdward = img("faces/IIA8HebelkaEdward.png")
IIA8HyzlovaKaterina = img("faces/IIA8HyzlovaKaterina.png")
IIA8KrumniklMartin = img("faces/IIA8KrumniklMartin.png")
IIA8KuceraMiroslav = img("faces/IIA8KuceraMiroslav.png")
IIA8LokocMartin = img("faces/IIA8LokocMartin.png")
IIA8MisurcovaMarie = img("faces/IIA8MisurcovaMarie.png")
IIA8OklestkovaZuzana = img("faces/IIA8OklestkovaZuzana.png")
IIA8PerneckaAnna = img("faces/IIA8PerneckaAnna.png")
IIA8PilkovaMagdalena = img("faces/IIA8PilkovaMagdalena.png")
IIA8PospisilovaAnna = img("faces/IIA8PospisilovaAnna.png")
IIA8ProtivanekVojtech = img("faces/IIA8ProtivanekVojtech.png")
IIA8SasinkaJaromir = img("faces/IIA8SasinkaJaromir.png")
IIA8SeckarovaVeronika = img("faces/IIA8SeckarovaVeronika.png")
IIA8SlukaOndrej = img("faces/IIA8SlukaOndrej.png")
IIA8SmerekFrantisek = img("faces/IIA8SmerekFrantisek.png")
IIA8SrovnalikovaSofie = img("faces/IIA8SrovnalikovaSofie.png")
IIA8TomankovaMahulena = img("faces/IIA8TomankovaMahulena.png")
IIA8UlicnyTOldrich = img("faces/IIA8UlicnyTOldrich.png")
IIA8VaclavikovaAnna = img("faces/IIA8VaclavikovaAnna.png")
IIA8VevodovaSofie = img("faces/IIA8VevodovaSofie.png")
IIA8ZubakSamuel = img("faces/IIA8ZubakSamuel.png")
IIB4CernyMichael = img("faces/IIB4CernyMichael.png")
IIB4FrantikMichael = img("faces/IIB4FrantikMichael.png")
IIB4HajkovaNela = img("faces/IIB4HajkovaNela.png")
IIB4HawigerStepan = img("faces/IIB4HawigerStepan.png")
IIB4HlusiZaneta = img("faces/IIB4HlusiZaneta.png")
IIB4HulmanAlexander = img("faces/IIB4HulmanAlexander.png")
IIB4KastilovaMichaela = img("faces/IIB4KastilovaMichaela.png")
IIB4LatalovaAgata = img("faces/IIB4LatalovaAgata.png")
IIB4LiskovaNatalie = img("faces/IIB4LiskovaNatalie.png")
IIB4LondaDavid = img("faces/IIB4LondaDavid.png")
IIB4MachasTomas = img("faces/IIB4MachasTomas.png")
IIB4MaderkovaTereza = img("faces/IIB4MaderkovaTereza.png")
IIB4MichalcovaMonika = img("faces/IIB4MichalcovaMonika.png")
IIB4PospisilAdam = img("faces/IIB4PospisilAdam.png")
IIB4RuzickovaJulie = img("faces/IIB4RuzickovaJulie.png")
IIB4SadilovaAneta = img("faces/IIB4SadilovaAneta.png")
IIB4SalkovaJitka = img("faces/IIB4SalkovaJitka.png")
IIB4SedlackovaKaterina = img("faces/IIB4SedlackovaKaterina.png")
IIB4SemianovaVeronika = img("faces/IIB4SemianovaVeronika.png")
IIB4SirokaTereza = img("faces/IIB4SirokaTereza.png")
IIB4SkacelMatej = img("faces/IIB4SkacelMatej.png")
IIB4SnajdarRadek = img("faces/IIB4SnajdarRadek.png")
IIB4SpacekVojtech = img("faces/IIB4SpacekVojtech.png")
IIB4StrizJan = img("faces/IIB4StrizJan.png")
IIB4ZemanekJan = img("faces/IIB4ZemanekJan.png")
IIB6BuchtikJan = img("faces/IIB6BuchtikJan.png")
IIB6FoukalovaNela = img("faces/IIB6FoukalovaNela.png")
IIB6FryblikovaDominika = img("faces/IIB6FryblikovaDominika.png")
IIB6FrysakovaKristyna = img("faces/IIB6FrysakovaKristyna.png")
IIB6HavlikovaSara = img("faces/IIB6HavlikovaSara.png")
IIB6HefkovaNela = img("faces/IIB6HefkovaNela.png")
IIB6HermanovskaKLinda = img("faces/IIB6HermanovskaKLinda.png")
IIB6KadlecFilip = img("faces/IIB6KadlecFilip.png")
IIB6KafetsioisNikiforos = img("faces/IIB6KafetsioisNikiforos.png")
IIB6KlobouckovaAdela = img("faces/IIB6KlobouckovaAdela.png")
IIB6KlvackovaEma = img("faces/IIB6KlvackovaEma.png")
IIB6KrumniklovaDora = img("faces/IIB6KrumniklovaDora.png")
IIB6LabancovaBarbora = img("faces/IIB6LabancovaBarbora.png")
IIB6MezlovaAnezka = img("faces/IIB6MezlovaAnezka.png")
IIB6MichnaMarek = img("faces/IIB6MichnaMarek.png")
IIB6NedomaOndrej = img("faces/IIB6NedomaOndrej.png")
IIB6NemravaStepan = img("faces/IIB6NemravaStepan.png")
IIB6NguyenovaHamy = img("faces/IIB6NguyenovaHamy.png")
IIB6OvacacikovaLucie = img("faces/IIB6OvacacikovaLucie.png")
IIB6QuinnSophieEllen = img("faces/IIB6QuinnSophieEllen.png")
IIB6SimonikovaSara = img("faces/IIB6SimonikovaSara.png")
IIB6SinclovaAnna = img("faces/IIB6SinclovaAnna.png")
IIB6StepanekJaroslav = img("faces/IIB6StepanekJaroslav.png")
IIB6StrakovaEma = img("faces/IIB6StrakovaEma.png")
IIB6TonnerovaENatalie = img("faces/IIB6TonnerovaENatalie.png")
IIB6VyskupSamuel = img("faces/IIB6VyskupSamuel.png")
IIC6BicLukas = img("faces/IIC6BicLukas.png")
IIC6BodnarVilem = img("faces/IIC6BodnarVilem.png")
IIC6HautlerPatrik = img("faces/IIC6HautlerPatrik.png")
IIC6HradilJan = img("faces/IIC6HradilJan.png")
IIC6JanicekMatyas = img("faces/IIC6JanicekMatyas.png")
IIC6KorcovaHana = img("faces/IIC6KorcovaHana.png")
IIC6KunstRichard = img("faces/IIC6KunstRichard.png")
IIC6KyselyMartin = img("faces/IIC6KyselyMartin.png")
IIC6LabounkovaKlara = img("faces/IIC6LabounkovaKlara.png")
IIC6PavlikMartin = img("faces/IIC6PavlikMartin.png")
IIC6PechovaLucie = img("faces/IIC6PechovaLucie.png")
IIC6PerinovaNikol = img("faces/IIC6PerinovaNikol.png")
IIC6PhanThiNhuMai = img("faces/IIC6PhanThiNhuMai.png")
IIC6RajnochDavid = img("faces/IIC6RajnochDavid.png")
IIC6SiskovaMarketa = img("faces/IIC6SiskovaMarketa.png")
IIC6SmeralovaTereza = img("faces/IIC6SmeralovaTereza.png")
IIC6SmitalMartin = img("faces/IIC6SmitalMartin.png")
IIC6SofronieskiAlex = img("faces/IIC6SofronieskiAlex.png")
IIC6StastnyRIchard = img("faces/IIC6StastnyRIchard.png")
IIC6SuchaTereza = img("faces/IIC6SuchaTereza.png")
IIC6SvrcekVojtech = img("faces/IIC6SvrcekVojtech.png")
IIC6TisonovaMarie = img("faces/IIC6TisonovaMarie.png")
IIIA4BizonPavel = img("faces/IIIA4BizonPavel.png")
IIIA4BrezovskyDaniel = img("faces/IIIA4BrezovskyDaniel.png")
IIIA4DzurianovaLucie = img("faces/IIIA4DzurianovaLucie.png")
IIIA4HavlovaKlara = img("faces/IIIA4HavlovaKlara.png")
IIIA4HorakovaNatalie = img("faces/IIIA4HorakovaNatalie.png")
IIIA4HorakStepan = img("faces/IIIA4HorakStepan.png")
IIIA4JakobBenjamin = img("faces/IIIA4JakobBenjamin.png")
IIIA4JanackovaLucie = img("faces/IIIA4JanackovaLucie.png")
IIIA4JenikovaMonika = img("faces/IIIA4JenikovaMonika.png")
IIIA4JurtikovaJarmila = img("faces/IIIA4JurtikovaJarmila.png")
IIIA4KalvachMichal = img("faces/IIIA4KalvachMichal.png")
IIIA4KnoflickovaJana = img("faces/IIIA4KnoflickovaJana.png")
IIIA4KozlovskaElena = img("faces/IIIA4KozlovskaElena.png")
IIIA4LatalovaNikola = img("faces/IIIA4LatalovaNikola.png")
IIIA4LatalovaZuzana = img("faces/IIIA4LatalovaZuzana.png")
IIIA4MajdiakJosef = img("faces/IIIA4MajdiakJosef.png")
IIIA4MonicovaKaterina = img("faces/IIIA4MonicovaKaterina.png")
IIIA4MudrakVit = img("faces/IIIA4MudrakVit.png")
IIIA4NeoralovaZuzana = img("faces/IIIA4NeoralovaZuzana.png")
IIIA4NevecnaSarka = img("faces/IIIA4NevecnaSarka.png")
IIIA4NezhybovaKristyna = img("faces/IIIA4NezhybovaKristyna.png")
IIIA4PallaJiri = img("faces/IIIA4PallaJiri.png")
IIIA4PichovaAndrea = img("faces/IIIA4PichovaAndrea.png")
IIIA4RudykovaAlexandra = img("faces/IIIA4RudykovaAlexandra.png")
IIIA4StimplovaMarketa = img("faces/IIIA4StimplovaMarketa.png")
IIIA4SuchankovaJasmina = img("faces/IIIA4SuchankovaJasmina.png")
IIIA4SvabenskaEliska = img("faces/IIIA4SvabenskaEliska.png")
IIIA4TelickaTobias = img("faces/IIIA4TelickaTobias.png")
IIIA4UtikalovaEliska = img("faces/IIIA4UtikalovaEliska.png")
IIIA4VitoulovaTereza = img("faces/IIIA4VitoulovaTereza.png")
IIIA4WeinlichovaNatalie = img("faces/IIIA4WeinlichovaNatalie.png")
JanickovaAjCj = img("faces/JanickovaAjCj.jpg")
JonesAj = img("faces/JonesAj.jpg")
JurikTvZ = img("faces/JurikTvZ.jpg")
KalandrovaCjOv = img("faces/KalandrovaCjOv.jpg")
KnapekAjSp = img("faces/KnapekAjSp.jpg")
KonecnaNeCj = img("faces/KonecnaNeCj.jpg")
KostkovaMaCh = img("faces/KostkovaMaCh.jpg")
KovarovaMaCh = img("faces/KovarovaMaCh.jpg")
KralovaAj = img("faces/KralovaAj.jpg")
KrcovaMaZ = img("faces/KrcovaMaZ.jpg")
KrejcirovaSp = img("faces/KrejcirovaSp.jpg")
KrejcirTvZ = img("faces/KrejcirTvZ.jpg")
KrizovaMaFy = img("faces/KrizovaMaFy.jpg")
KvapilMaFyHv = img("faces/KvapilMaFyHv.jpg")
LekesovaCjHv = img("faces/LekesovaCjHv.jpg")
LetakovaBiCh = img("faces/LetakovaBiCh.jpg")
MadrovaAj = img("faces/MadrovaAj.jpg")
MarkovaBiCh = img("faces/MarkovaBiCh.jpg")
MartinikovaNeHv = img("faces/MartinikovaNeHv.jpg")
MasnyOvVv = img("faces/MasnyOvVv.jpg")
McMullinAj = img("faces/McMullinAj.jpg")
MenouskovaCjFr = img("faces/MenouskovaCjFr.jpg")
MinarikMa = img("faces/MinarikMa.jpg")
NavratilBiZ = img("faces/NavratilBiZ.jpg")
NavratilovaAj = img("faces/NavratilovaAj.jpg")
NezvalovaAjRuD = img("faces/NezvalovaAjRuD.jpg")
OndrakOvLat = img("faces/OndrakOvLat.jpg")
PazderovaMaFy = img("faces/PazderovaMaFy.jpg")
PetrMaFy = img("faces/PetrMaFy.jpg")
PiechovaAj = img("faces/PiechovaAj.jpg")
PohanelMaZAjProjekty = img("faces/PohanelMaZAjProjekty.jpg")
PolednovaMaZ = img("faces/PolednovaMaZ.jpg")
PridalovaAjRu = img("faces/PridalovaAjRu.jpg")
PrzybylovaCjHv = img("faces/PrzybylovaCjHv.jpg")
PuskarovaNeCj = img("faces/PuskarovaNeCj.jpg")
RehulkaBiCh = img("faces/RehulkaBiCh.jpg")
RichterkovaMaFy = img("faces/RichterkovaMaFy.jpg")
SedlackovaCjFr = img("faces/SedlackovaCjFr.jpg")
SeverovaMaIVT = img("faces/SeverovaMaIVT.jpg")
SladecekCjAj = img("faces/SladecekCjAj.jpg")
SoubustovaNeRu = img("faces/SoubustovaNeRu.jpg")
StanecSp = img("faces/StanecSp.jpg")
StepanovIVT = img("faces/StepanovIVT.jpg")
StranskaFy = img("faces/StranskaFy.jpg")
StudnickaMaIVT = img("faces/StudnickaMaIVT.jpg")
SuchankovaAj = img("faces/SuchankovaAj.jpg")
SykorovaAjD = img("faces/SykorovaAjD.jpg")
TeplyAjTv = img("faces/TeplyAjTv.jpg")
UrbaskovaMaZ = img("faces/UrbaskovaMaZ.jpg")
VackovaCjVVEkonomie = img("faces/VackovaCjVVEkonomie.jpg")
VasiljevovaBiVV = img("faces/VasiljevovaBiVV.jpg")
VavraCjVV = img("faces/VavraCjVV.jpg")
VeselaCjNe = img("faces/VeselaCjNe.jpg")
VitamvasovaAj = img("faces/VitamvasovaAj.jpg")
VojtovicovaMaFyAj = img("faces/VojtovicovaMaFyAj.jpg")
ZabojovaBiCh = img("faces/ZabojovaBiCh.jpg")
ZajicovaCjNe = img("faces/ZajicovaCjNe.jpg")
ZarubovaMaCh = img("faces/ZarubovaMaCh.jpg")
ZatloukalovaVVRu = img("faces/ZatloukalovaVVRu.jpg")
known_face_encodings = [AbrahamovaTv, Adamikova2AjRuD, BednarikovaMaITV, BerankovaAjFr, BraunerChBi, CastellarSp, CechovaAj, ChromaTvZ, DanielTvZ, DohnalovaCjHv, DostalovaTv, DubovaNeCj, DvorskyAjD, FaberovaAjRu, FerencMaFy, FukaCjNe, GlosCjD, HajduMaAj, HajekBiCh, HamrikovaMaCh, HavranovaAj, HermanovaCjHvRu, HorvathSp, HubackovaCjD, IA4BerkovaAnna, IA4BilikovaAlzbeta, IA4BrstakovaJulie, IA4BubenickovaAneta, IA4BuczkovaBarbora, IA4ChmelikLukas, IA4DankovaKarolina, IA4GalnorJakub, IA4GjurgjealaKaona, IA4HalovaBarbora, IA4HimrMatej, IA4HodurovaKEliska, IA4JanalikTomas, IA4KostkaJan, IA4KoukalFrantisek, IA4KrejciMatyas, IA4LipkovaValerie, IA4LosikLeonard, IA4MachovaDagmar, IA4PolednaJan, IA4StavarskaLucie, IA4StechovaBarbora, IA4StejskalovaLinda, IA4VaculikPetr, IA4WestphalDavid, IA6BaresovaKlara, IA6BelohlavkovaMarie, IA6CapalovaKarolina, IA6FedorcoMarian, IA6FilousovaLena, IA6HorklovaKatka, IA6KlosovaMarie, IA6KvapilMichael, IA6LukasovaAdela, IA6MachStepan, IA6MaslikovaTereza, IA6NavratilJachym, IA6PridalMatej, IA6PtackovaEliska, IA6SimakStepan, IA6SouckovaSara, IA6SouckovaZdenka, IA6SouskovaEliska, IA6StarostovaTereza, IA6StybnarMarek, IA6SvobodaDavid, IA6UherJan, IA6ValekDan, IA6VrajovaJana, IA6VyroubalRadek, IA6WittmannovaJAnna, IA6ZelenkovaTereza, IA6ZemberovaDaniela, IA8AuxtovaLinda, IA8BartosJan, IA8BenesovaJohana, IA8BouchalovaKveta, IA8ChmelovaVendula, IA8CisarVojtech, IA8DostalJakub, IA8FilousovaAlzbeta, IA8GajdusekMiroslav, IA8GogolJMatyas, IA8GrassovaEla, IA8HalatovaVeronika, IA8HandlovaKaterina, IA8HarnosovaAlzbeta, IA8HulikovaAmelie, IA8IlleovaAdela, IA8JensDavid, IA8KmentovaMarie, IA8KornhonTomas, IA8KropacDavid, IA8LonicekMartin, IA8MaslikovaKarolina, IA8MohylovaLaura, IA8MuchovaJohana, IA8NavratilDaniel, IA8ProchazkaJan, IA8StefanuttovaAmalie, IA8SterbovaSDana, IA8TichyMaxmilian, IA8ZdrazilovaAKarolina, IB4ApplovaPavlina, IB4BacikZeyner, IB4HavlikMatyas, IB4HrancovaMarketa, IB4HrnkovaGita, IB4JarosMichael, IB4KalabisovaAnna, IB4KejklickovaTereza, IB4MachVKrystof, IB4MadrovaAdriana, IB4MalaLenka, IB4MykhailetsVadim, IB4PopelkaStepan, IB4PospisilovaZuzana, IB4PrincDaniel, IB4SalamonJan, IB4SittekJakub, IB4SkladanyLukas, IB4SkrontovaEliska, IB4SkurkovaAdela, IB4SpevakovaEva, IB4StojakovaLucie, IB4StolfovaNatalie, IB4TajovskaNikola, IB4VejmolovaKarolina, IB6BrodaJakub, IB6CventanovaKaterina, IB6FisaraDavid, IB6KonecnaLucie, IB6KonecnyVit, IB6KriegovaPavlina, IB6KrizAntonin, IB6KubelkaErik, IB6LejskovaAdela, IB6LosikovaLada, IB6MacickovaJana, IB6MiksikovaNatalie, IB6MikulovaBerenika, IB6NajerMarek, IB6NepovimovaLucie, IB6NovotnyOndrej, IB6PribylVojtech, IB6RobertsonTomas, IB6RybaFrantisek, IB6SedajovaSarka, IB6SobekTomas, IB6SohnelDavid, IB6StefanovaEma, IB6StrnadelMichael, IB6SyrovatkovaEliska, IB6UrbamkovaAnezka, IB6UtikalovaLLeontyna, IB6VohankovaKlara, IB6ZborilovaSara, IB8BrundaMikulas, IB8BurdaJan, IB8ChrasteckyJan, IB8DoubalovaJarmila, IB8FischerOndrej, IB8GastaPetr, IB8IloemezueBeaAdachi, IB8KlimcakRichard, IB8KonecnaElla, IB8KubickovaSofire, IB8KubikJachym, IB8LacovaKristina, IB8LinekOndrej, IB8MachacovaEdita, IB8MorbicrovaAdela, IB8NgoTuongVan, IB8OndrouskovaTereza, IB8OpavskyVit, IB8PeterovaMichaela, IB8PiechDaniel, IB8RaabovaIva, IB8StoppenovaJulie, IB8TisovskyMikulas, IB8UtikalovaNJustyna, IB8VelickyVaclav, IB8VodickovaKristyna, IB8ZavadilTomas, IB8ZdarilDaniel, IIA4AndršJan, IIA4BiskupovaSimona, IIA4BlumaJan, IIA4ChodurkovaAnna, IIA4ChytilovaKarolina, IIA4DrahotuskaAmalie, IIA4DvorskaVeronika, IIA4FrancakovaKarla, IIA4FrkalFIlip, IIA4FrumarovaAdela, IIA4HolikovaNatalie, IIA4HrabalovaKlara, IIA4HrbackovaKristyna, IIA4HrbatovaEva, IIA4HunovaDenisa, IIA4JancikovaLucie, IIA4JanecekJakub, IIA4KudybBenjamin, IIA4LekešMatyas, IIA4MatejJiri, IIA4MikulkaPetr, IIA4NemecJakub, IIA4PekarJakub, IIA4SaladakTobias, IIA4SevernakovaVeronika, IIA4SmetakMarek, IIA4ZymovaAneta, IIA6BazgerovaEllen, IIA6DolezalovaElla, IIA6DracJan, IIA6DreslerVaclva, IIA6FilipovaKarolina, IIA6FrybortovaElisa, IIA6HamalovaAlzbeta, IIA6HomolacovaDarina, IIA6HorakovaEma, IIA6HorvathMatus, IIA6KolousekMarek, IIA6KysucanovaMilena, IIA6LerchStepan, IIA6MaskovaEEmma, IIA6PavelkovaZuzana, IIA6PilchovaZuzana, IIA6PlesnikAdam, IIA6SvetlikovaEma, IIA6TranNguyenHongMai, IIA6VaclavikovaNicol, IIA6VitkovaAneta, IIA6VlkovaEliska, IIA6VrtalovaPetra, IIA6WiedermannovaEla, IIA6ZatloukalovaNela, IIA6ZeitlerSamuel, IIA6ZidkovaBarbora, IIA8BalnerJakub, IIA8CablikovaAnna, IIA8CernaStella, IIA8CoufalovaBerenika, IIA8DupalovaMichaela, IIA8HajekKrystof, IIA8HamplJonas, IIA8HebelkaEdward, IIA8HyzlovaKaterina, IIA8KrumniklMartin, IIA8KuceraMiroslav, IIA8LokocMartin, IIA8MisurcovaMarie, IIA8OklestkovaZuzana, IIA8PerneckaAnna, IIA8PilkovaMagdalena, IIA8PospisilovaAnna, IIA8ProtivanekVojtech, IIA8SasinkaJaromir, IIA8SeckarovaVeronika, IIA8SlukaOndrej, IIA8SmerekFrantisek, IIA8SrovnalikovaSofie, IIA8TomankovaMahulena, IIA8UlicnyTOldrich, IIA8VaclavikovaAnna, IIA8VevodovaSofie, IIA8ZubakSamuel, IIB4CernyMichael, IIB4FrantikMichael, IIB4HajkovaNela, IIB4HawigerStepan, IIB4HlusiZaneta, IIB4HulmanAlexander, IIB4KastilovaMichaela, IIB4LatalovaAgata, IIB4LiskovaNatalie, IIB4LondaDavid, IIB4MachasTomas, IIB4MaderkovaTereza, IIB4MichalcovaMonika, IIB4PospisilAdam, IIB4RuzickovaJulie, IIB4SadilovaAneta, IIB4SalkovaJitka, IIB4SedlackovaKaterina, IIB4SemianovaVeronika, IIB4SirokaTereza, IIB4SkacelMatej, IIB4SnajdarRadek, IIB4SpacekVojtech, IIB4StrizJan, IIB4ZemanekJan, IIB6BuchtikJan, IIB6FoukalovaNela, IIB6FryblikovaDominika, IIB6FrysakovaKristyna, IIB6HavlikovaSara, IIB6HefkovaNela, IIB6HermanovskaKLinda, IIB6KadlecFilip, IIB6KafetsioisNikiforos, IIB6KlobouckovaAdela, IIB6KlvackovaEma, IIB6KrumniklovaDora, IIB6LabancovaBarbora, IIB6MezlovaAnezka, IIB6MichnaMarek, IIB6NedomaOndrej, IIB6NemravaStepan, IIB6NguyenovaHamy, IIB6OvacacikovaLucie, IIB6QuinnSophieEllen, IIB6SimonikovaSara, IIB6SinclovaAnna, IIB6StepanekJaroslav, IIB6StrakovaEma, IIB6TonnerovaENatalie, IIB6VyskupSamuel, IIC6BicLukas, IIC6BodnarVilem, IIC6HautlerPatrik, IIC6HradilJan, IIC6JanicekMatyas, IIC6KorcovaHana, IIC6KunstRichard, IIC6KyselyMartin, IIC6LabounkovaKlara, IIC6PavlikMartin, IIC6PechovaLucie, IIC6PerinovaNikol, IIC6PhanThiNhuMai, IIC6RajnochDavid, IIC6SiskovaMarketa, IIC6SmeralovaTereza, IIC6SmitalMartin, IIC6SofronieskiAlex, IIC6StastnyRIchard, IIC6SuchaTereza, IIC6SvrcekVojtech, IIC6TisonovaMarie, IIIA4BizonPavel, IIIA4BrezovskyDaniel, IIIA4DzurianovaLucie, IIIA4HavlovaKlara, IIIA4HorakovaNatalie, IIIA4HorakStepan, IIIA4JakobBenjamin, IIIA4JanackovaLucie, IIIA4JenikovaMonika, IIIA4JurtikovaJarmila, IIIA4KalvachMichal, IIIA4KnoflickovaJana, IIIA4KozlovskaElena, IIIA4LatalovaNikola, IIIA4LatalovaZuzana, IIIA4MajdiakJosef, IIIA4MonicovaKaterina, IIIA4MudrakVit, IIIA4NeoralovaZuzana, IIIA4NevecnaSarka, IIIA4NezhybovaKristyna, IIIA4PallaJiri, IIIA4PichovaAndrea, IIIA4RudykovaAlexandra, IIIA4StimplovaMarketa, IIIA4SuchankovaJasmina, IIIA4SvabenskaEliska, IIIA4TelickaTobias, IIIA4UtikalovaEliska, IIIA4VitoulovaTereza, IIIA4WeinlichovaNatalie, JanickovaAjCj, JonesAj, JurikTvZ, KalandrovaCjOv, KnapekAjSp, KonecnaNeCj, KostkovaMaCh, KovarovaMaCh, KralovaAj, KrcovaMaZ, KrejcirovaSp, KrejcirTvZ, KrizovaMaFy, KvapilMaFyHv, LekesovaCjHv, LetakovaBiCh, MadrovaAj, MarkovaBiCh, MartinikovaNeHv, MasnyOvVv, McMullinAj, MenouskovaCjFr, MinarikMa, NavratilBiZ, NavratilovaAj, NezvalovaAjRuD, OndrakOvLat, PazderovaMaFy, PetrMaFy, PiechovaAj, PohanelMaZAjProjekty, PolednovaMaZ, PridalovaAjRu, PrzybylovaCjHv, PuskarovaNeCj, RehulkaBiCh, RichterkovaMaFy, SedlackovaCjFr, SeverovaMaIVT, SladecekCjAj, SoubustovaNeRu, StanecSp, StepanovIVT, StranskaFy, StudnickaMaIVT, SuchankovaAj, SykorovaAjD, TeplyAjTv, UrbaskovaMaZ, VackovaCjVVEkonomie, VasiljevovaBiVV, VavraCjVV, VeselaCjNe, VitamvasovaAj, VojtovicovaMaFyAj, ZabojovaBiCh, ZajicovaCjNe, ZarubovaMaCh, ZatloukalovaVVRu]
known_face_names = ['AbrahamovaTv', 'Adamikova2AjRuD', 'BednarikovaMaITV', 'BerankovaAjFr', 'BraunerChBi', 'CastellarSp', 'CechovaAj', 'ChromaTvZ', 'DanielTvZ', 'DohnalovaCjHv', 'DostalovaTv', 'DubovaNeCj', 'DvorskyAjD', 'FaberovaAjRu', 'FerencMaFy', 'FukaCjNe', 'GlosCjD', 'HajduMaAj', 'HajekBiCh', 'HamrikovaMaCh', 'HavranovaAj', 'HermanovaCjHvRu', 'HorvathSp', 'HubackovaCjD', 'IA4BerkovaAnna', 'IA4BilikovaAlzbeta', 'IA4BrstakovaJulie', 'IA4BubenickovaAneta', 'IA4BuczkovaBarbora', 'IA4ChmelikLukas', 'IA4DankovaKarolina', 'IA4GalnorJakub', 'IA4GjurgjealaKaona', 'IA4HalovaBarbora', 'IA4HimrMatej', 'IA4HodurovaKEliska', 'IA4JanalikTomas', 'IA4KostkaJan', 'IA4KoukalFrantisek', 'IA4KrejciMatyas', 'IA4LipkovaValerie', 'IA4LosikLeonard', 'IA4MachovaDagmar', 'IA4PolednaJan', 'IA4StavarskaLucie', 'IA4StechovaBarbora', 'IA4StejskalovaLinda', 'IA4VaculikPetr', 'IA4WestphalDavid', 'IA6BaresovaKlara', 'IA6BelohlavkovaMarie', 'IA6CapalovaKarolina', 'IA6FedorcoMarian', 'IA6FilousovaLena', 'IA6HorklovaKatka', 'IA6KlosovaMarie', 'IA6KvapilMichael', 'IA6LukasovaAdela', 'IA6MachStepan', 'IA6MaslikovaTereza', 'IA6NavratilJachym', 'IA6PridalMatej', 'IA6PtackovaEliska', 'IA6SimakStepan', 'IA6SouckovaSara', 'IA6SouckovaZdenka', 'IA6SouskovaEliska', 'IA6StarostovaTereza', 'IA6StybnarMarek', 'IA6SvobodaDavid', 'IA6UherJan', 'IA6ValekDan', 'IA6VrajovaJana', 'IA6VyroubalRadek', 'IA6WittmannovaJAnna', 'IA6ZelenkovaTereza', 'IA6ZemberovaDaniela', 'IA8AuxtovaLinda', 'IA8BartosJan', 'IA8BenesovaJohana', 'IA8BouchalovaKveta', 'IA8ChmelovaVendula', 'IA8CisarVojtech', 'IA8DostalJakub', 'IA8FilousovaAlzbeta', 'IA8GajdusekMiroslav', 'IA8GogolJMatyas', 'IA8GrassovaEla', 'IA8HalatovaVeronika', 'IA8HandlovaKaterina', 'IA8HarnosovaAlzbeta', 'IA8HulikovaAmelie', 'IA8IlleovaAdela', 'IA8JensDavid', 'IA8KmentovaMarie', 'IA8KornhonTomas', 'IA8KropacDavid', 'IA8LonicekMartin', 'IA8MaslikovaKarolina', 'IA8MohylovaLaura', 'IA8MuchovaJohana', 'IA8NavratilDaniel', 'IA8ProchazkaJan', 'IA8StefanuttovaAmalie', 'IA8SterbovaSDana', 'IA8TichyMaxmilian', 'IA8ZdrazilovaAKarolina', 'IB4ApplovaPavlina', 'IB4BacikZeyner', 'IB4HavlikMatyas', 'IB4HrancovaMarketa', 'IB4HrnkovaGita', 'IB4JarosMichael', 'IB4KalabisovaAnna', 'IB4KejklickovaTereza', 'IB4MachVKrystof', 'IB4MadrovaAdriana', 'IB4MalaLenka', 'IB4MykhailetsVadim', 'IB4PopelkaStepan', 'IB4PospisilovaZuzana', 'IB4PrincDaniel', 'IB4SalamonJan', 'IB4SittekJakub', 'IB4SkladanyLukas', 'IB4SkrontovaEliska', 'IB4SkurkovaAdela', 'IB4SpevakovaEva', 'IB4StojakovaLucie', 'IB4StolfovaNatalie', 'IB4TajovskaNikola', 'IB4VejmolovaKarolina', 'IB6BrodaJakub', 'IB6CventanovaKaterina', 'IB6FisaraDavid', 'IB6KonecnaLucie', 'IB6KonecnyVit', 'IB6KriegovaPavlina', 'IB6KrizAntonin', 'IB6KubelkaErik', 'IB6LejskovaAdela', 'IB6LosikovaLada', 'IB6MacickovaJana', 'IB6MiksikovaNatalie', 'IB6MikulovaBerenika', 'IB6NajerMarek', 'IB6NepovimovaLucie', 'IB6NovotnyOndrej', 'IB6PribylVojtech', 'IB6RobertsonTomas', 'IB6RybaFrantisek', 'IB6SedajovaSarka', 'IB6SobekTomas', 'IB6SohnelDavid', 'IB6StefanovaEma', 'IB6StrnadelMichael', 'IB6SyrovatkovaEliska', 'IB6UrbamkovaAnezka', 'IB6UtikalovaLLeontyna', 'IB6VohankovaKlara', 'IB6ZborilovaSara', 'IB8BrundaMikulas', 'IB8BurdaJan', 'IB8ChrasteckyJan', 'IB8DoubalovaJarmila', 'IB8FischerOndrej', 'IB8GastaPetr', 'IB8IloemezueBeaAdachi', 'IB8KlimcakRichard', 'IB8KonecnaElla', 'IB8KubickovaSofire', 'IB8KubikJachym', 'IB8LacovaKristina', 'IB8LinekOndrej', 'IB8MachacovaEdita', 'IB8MorbicrovaAdela', 'IB8NgoTuongVan', 'IB8OndrouskovaTereza', 'IB8OpavskyVit', 'IB8PeterovaMichaela', 'IB8PiechDaniel', 'IB8RaabovaIva', 'IB8StoppenovaJulie', 'IB8TisovskyMikulas', 'IB8UtikalovaNJustyna', 'IB8VelickyVaclav', 'IB8VodickovaKristyna', 'IB8ZavadilTomas', 'IB8ZdarilDaniel', 'IIA4AndršJan', 'IIA4BiskupovaSimona', 'IIA4BlumaJan', 'IIA4ChodurkovaAnna', 'IIA4ChytilovaKarolina', 'IIA4DrahotuskaAmalie', 'IIA4DvorskaVeronika', 'IIA4FrancakovaKarla', 'IIA4FrkalFIlip', 'IIA4FrumarovaAdela', 'IIA4HolikovaNatalie', 'IIA4HrabalovaKlara', 'IIA4HrbackovaKristyna', 'IIA4HrbatovaEva', 'IIA4HunovaDenisa', 'IIA4JancikovaLucie', 'IIA4JanecekJakub', 'IIA4KudybBenjamin', 'IIA4LekešMatyas', 'IIA4MatejJiri', 'IIA4MikulkaPetr', 'IIA4NemecJakub', 'IIA4PekarJakub', 'IIA4SaladakTobias', 'IIA4SevernakovaVeronika', 'IIA4SmetakMarek', 'IIA4ZymovaAneta', 'IIA6BazgerovaEllen', 'IIA6DolezalovaElla', 'IIA6DracJan', 'IIA6DreslerVaclva', 'IIA6FilipovaKarolina', 'IIA6FrybortovaElisa', 'IIA6HamalovaAlzbeta', 'IIA6HomolacovaDarina', 'IIA6HorakovaEma', 'IIA6HorvathMatus', 'IIA6KolousekMarek', 'IIA6KysucanovaMilena', 'IIA6LerchStepan', 'IIA6MaskovaEEmma', 'IIA6PavelkovaZuzana', 'IIA6PilchovaZuzana', 'IIA6PlesnikAdam', 'IIA6SvetlikovaEma', 'IIA6TranNguyenHongMai', 'IIA6VaclavikovaNicol', 'IIA6VitkovaAneta', 'IIA6VlkovaEliska', 'IIA6VrtalovaPetra', 'IIA6WiedermannovaEla', 'IIA6ZatloukalovaNela', 'IIA6ZeitlerSamuel', 'IIA6ZidkovaBarbora', 'IIA8BalnerJakub', 'IIA8CablikovaAnna', 'IIA8CernaStella', 'IIA8CoufalovaBerenika', 'IIA8DupalovaMichaela', 'IIA8HajekKrystof', 'IIA8HamplJonas', 'IIA8HebelkaEdward', 'IIA8HyzlovaKaterina', 'IIA8KrumniklMartin', 'IIA8KuceraMiroslav', 'IIA8LokocMartin', 'IIA8MisurcovaMarie', 'IIA8OklestkovaZuzana', 'IIA8PerneckaAnna', 'IIA8PilkovaMagdalena', 'IIA8PospisilovaAnna', 'IIA8ProtivanekVojtech', 'IIA8SasinkaJaromir', 'IIA8SeckarovaVeronika', 'IIA8SlukaOndrej', 'IIA8SmerekFrantisek', 'IIA8SrovnalikovaSofie', 'IIA8TomankovaMahulena', 'IIA8UlicnyTOldrich', 'IIA8VaclavikovaAnna', 'IIA8VevodovaSofie', 'IIA8ZubakSamuel', 'IIB4CernyMichael', 'IIB4FrantikMichael', 'IIB4HajkovaNela', 'IIB4HawigerStepan', 'IIB4HlusiZaneta', 'IIB4HulmanAlexander', 'IIB4KastilovaMichaela', 'IIB4LatalovaAgata', 'IIB4LiskovaNatalie', 'IIB4LondaDavid', 'IIB4MachasTomas', 'IIB4MaderkovaTereza', 'IIB4MichalcovaMonika', 'IIB4PospisilAdam', 'IIB4RuzickovaJulie', 'IIB4SadilovaAneta', 'IIB4SalkovaJitka', 'IIB4SedlackovaKaterina', 'IIB4SemianovaVeronika', 'IIB4SirokaTereza', 'IIB4SkacelMatej', 'IIB4SnajdarRadek', 'IIB4SpacekVojtech', 'IIB4StrizJan', 'IIB4ZemanekJan', 'IIB6BuchtikJan', 'IIB6FoukalovaNela', 'IIB6FryblikovaDominika', 'IIB6FrysakovaKristyna', 'IIB6HavlikovaSara', 'IIB6HefkovaNela', 'IIB6HermanovskaKLinda', 'IIB6KadlecFilip', 'IIB6KafetsioisNikiforos', 'IIB6KlobouckovaAdela', 'IIB6KlvackovaEma', 'IIB6KrumniklovaDora', 'IIB6LabancovaBarbora', 'IIB6MezlovaAnezka', 'IIB6MichnaMarek', 'IIB6NedomaOndrej', 'IIB6NemravaStepan', 'IIB6NguyenovaHamy', 'IIB6OvacacikovaLucie', 'IIB6QuinnSophieEllen', 'IIB6SimonikovaSara', 'IIB6SinclovaAnna', 'IIB6StepanekJaroslav', 'IIB6StrakovaEma', 'IIB6TonnerovaENatalie', 'IIB6VyskupSamuel', 'IIC6BicLukas', 'IIC6BodnarVilem', 'IIC6HautlerPatrik', 'IIC6HradilJan', 'IIC6JanicekMatyas', 'IIC6KorcovaHana', 'IIC6KunstRichard', 'IIC6KyselyMartin', 'IIC6LabounkovaKlara', 'IIC6PavlikMartin', 'IIC6PechovaLucie', 'IIC6PerinovaNikol', 'IIC6PhanThiNhuMai', 'IIC6RajnochDavid', 'IIC6SiskovaMarketa', 'IIC6SmeralovaTereza', 'IIC6SmitalMartin', 'IIC6SofronieskiAlex', 'IIC6StastnyRIchard', 'IIC6SuchaTereza', 'IIC6SvrcekVojtech', 'IIC6TisonovaMarie', 'IIIA4BizonPavel', 'IIIA4BrezovskyDaniel', 'IIIA4DzurianovaLucie', 'IIIA4HavlovaKlara', 'IIIA4HorakovaNatalie', 'IIIA4HorakStepan', 'IIIA4JakobBenjamin', 'IIIA4JanackovaLucie', 'IIIA4JenikovaMonika', 'IIIA4JurtikovaJarmila', 'IIIA4KalvachMichal', 'IIIA4KnoflickovaJana', 'IIIA4KozlovskaElena', 'IIIA4LatalovaNikola', 'IIIA4LatalovaZuzana', 'IIIA4MajdiakJosef', 'IIIA4MonicovaKaterina', 'IIIA4MudrakVit', 'IIIA4NeoralovaZuzana', 'IIIA4NevecnaSarka', 'IIIA4NezhybovaKristyna', 'IIIA4PallaJiri', 'IIIA4PichovaAndrea', 'IIIA4RudykovaAlexandra', 'IIIA4StimplovaMarketa', 'IIIA4SuchankovaJasmina', 'IIIA4SvabenskaEliska', 'IIIA4TelickaTobias', 'IIIA4UtikalovaEliska', 'IIIA4VitoulovaTereza', 'IIIA4WeinlichovaNatalie', 'JanickovaAjCj', 'JonesAj', 'JurikTvZ', 'KalandrovaCjOv', 'KnapekAjSp', 'KonecnaNeCj', 'KostkovaMaCh', 'KovarovaMaCh', 'KralovaAj', 'KrcovaMaZ', 'KrejcirovaSp', 'KrejcirTvZ', 'KrizovaMaFy', 'KvapilMaFyHv', 'LekesovaCjHv', 'LetakovaBiCh', 'MadrovaAj', 'MarkovaBiCh', 'MartinikovaNeHv', 'MasnyOvVv', 'McMullinAj', 'MenouskovaCjFr', 'MinarikMa', 'NavratilBiZ', 'NavratilovaAj', 'NezvalovaAjRuD', 'OndrakOvLat', 'PazderovaMaFy', 'PetrMaFy', 'PiechovaAj', 'PohanelMaZAjProjekty', 'PolednovaMaZ', 'PridalovaAjRu', 'PrzybylovaCjHv', 'PuskarovaNeCj', 'RehulkaBiCh', 'RichterkovaMaFy', 'SedlackovaCjFr', 'SeverovaMaIVT', 'SladecekCjAj', 'SoubustovaNeRu', 'StanecSp', 'StepanovIVT', 'StranskaFy', 'StudnickaMaIVT', 'SuchankovaAj', 'SykorovaAjD', 'TeplyAjTv', 'UrbaskovaMaZ', 'VackovaCjVVEkonomie', 'VasiljevovaBiVV', 'VavraCjVV', 'VeselaCjNe', 'VitamvasovaAj', 'VojtovicovaMaFyAj', 'ZabojovaBiCh', 'ZajicovaCjNe', 'ZarubovaMaCh', 'ZatloukalovaVVRu']



print("pictures loaded")
print(time.time() - Start)
# Initialize some variables
multipl = 2
resize = 1 / multipl
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
print("variables")
loop_noob = 0
while True:
    loop_noob = loop_noob + 1
    # Grab a single frame of video
    ret, frame = video_capture.read()
    frame = cv2.resize(frame, (960, 540))
    print(ret, loop_noob)

    # Resize frame of video to 1/4 size for faster face recognition processing
    # small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    small_frame = cv2.resize(frame, (0, 0), fx=resize, fy=resize)
    # small_frame = frame

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        # top *= 4
        # right *= 4
        # bottom *= 4
        # left *= 4
        top *= multipl
        right *= multipl
        bottom *= multipl
        left *= multipl

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (255, 0, 0), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255 ), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
 