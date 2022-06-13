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
IIIA8BazantovaMagdalena = img("faces/IIIA8BazantovaMagdalena.png")
IIIA8BlahutovaEKarolina = img("faces/IIIA8BlahutovaEKarolina.png")
IIIA8BodnarovaEma = img("faces/IIIA8BodnarovaEma.png")
IIIA8BubenicekDavid = img("faces/IIIA8BubenicekDavid.png")
IIIA8DejlMartin = img("faces/IIIA8DejlMartin.png")
IIIA8DrozdovaNela = img("faces/IIIA8DrozdovaNela.png")
IIIA8DudaBenjamin = img("faces/IIIA8DudaBenjamin.png")
IIIA8DvorakovaTereza = img("faces/IIIA8DvorakovaTereza.png")
IIIA8FiserovaJana = img("faces/IIIA8FiserovaJana.png")
IIIA8HoangovaAnh = img("faces/IIIA8HoangovaAnh.png")
IIIA8HolasekTomas = img("faces/IIIA8HolasekTomas.png")
IIIA8HorakAlexandr = img("faces/IIIA8HorakAlexandr.png")
IIIA8HrabalNikola = img("faces/IIIA8HrabalNikola.png")
IIIA8JanosikLukas = img("faces/IIIA8JanosikLukas.png")
IIIA8KralovaIvana = img("faces/IIIA8KralovaIvana.png")
IIIA8KratkyLukas = img("faces/IIIA8KratkyLukas.png")
IIIA8KubikovaEliska = img("faces/IIIA8KubikovaEliska.png")
IIIA8KudlaRudolf = img("faces/IIIA8KudlaRudolf.png")
IIIA8KvapilovaTereza = img("faces/IIIA8KvapilovaTereza.png")
IIIA8MutinaMarek = img("faces/IIIA8MutinaMarek.png")
IIIA8MyskovaTereza = img("faces/IIIA8MyskovaTereza.png")
IIIA8NovakovaDaniela = img("faces/IIIA8NovakovaDaniela.png")
IIIA8SlezarovaAnna = img("faces/IIIA8SlezarovaAnna.png")
IIIA8SmekalovaLucie = img("faces/IIIA8SmekalovaLucie.png")
IIIA8StavarskyRichard = img("faces/IIIA8StavarskyRichard.png")
IIIA8ValentovaVeronika = img("faces/IIIA8ValentovaVeronika.png")
IIIA8VohralikovaJohana = img("faces/IIIA8VohralikovaJohana.png")
IIIA8ZikmundovaAdela = img("faces/IIIA8ZikmundovaAdela.png")
IIIB8AmbrosMichael = img("faces/IIIB8AmbrosMichael.png")
IIIB8AxmanovaPavlina = img("faces/IIIB8AxmanovaPavlina.png")
IIIB8BuresEBenjamin = img("faces/IIIB8BuresEBenjamin.png")
IIIB8CoufalovaNoemi = img("faces/IIIB8CoufalovaNoemi.png")
IIIB8DolezalovaHelena = img("faces/IIIB8DolezalovaHelena.png")
IIIB8HavrlantSimon = img("faces/IIIB8HavrlantSimon.png")
IIIB8HimrJonas = img("faces/IIIB8HimrJonas.png")
IIIB8HockadaySMatthew = img("faces/IIIB8HockadaySMatthew.png")
IIIB8HoudekJan = img("faces/IIIB8HoudekJan.png")
IIIB8JuraskovaAneta = img("faces/IIIB8JuraskovaAneta.png")
IIIB8KlimkovaViola = img("faces/IIIB8KlimkovaViola.png")
IIIB8KolarJan = img("faces/IIIB8KolarJan.png")
IIIB8KonecnyPetr = img("faces/IIIB8KonecnyPetr.png")
IIIB8LazarovaSofie = img("faces/IIIB8LazarovaSofie.png")
IIIB8MadrovaGabriela = img("faces/IIIB8MadrovaGabriela.png")
IIIB8PaulickovaTereza = img("faces/IIIB8PaulickovaTereza.png")
IIIB8PetrivalskyNil = img("faces/IIIB8PetrivalskyNil.png")
IIIB8PolednovaSofie = img("faces/IIIB8PolednovaSofie.png")
IIIB8RatajovaTerezie = img("faces/IIIB8RatajovaTerezie.png")
IIIB8SaradinMatej = img("faces/IIIB8SaradinMatej.png")
IIIB8SimackovaMEmma = img("faces/IIIB8SimackovaMEmma.png")
IIIB8SitovaHana = img("faces/IIIB8SitovaHana.png")
IIIB8SmutnaHana = img("faces/IIIB8SmutnaHana.png")
IIIB8StefanovaAnna = img("faces/IIIB8StefanovaAnna.png")
IIIB8StyblovaTatiana = img("faces/IIIB8StyblovaTatiana.png")
IIIB8TomeckovaAnna = img("faces/IIIB8TomeckovaAnna.png")
IIIB8VaclavikovaAnna = img("faces/IIIB8VaclavikovaAnna.png")
IIIB8VeseckyJakub = img("faces/IIIB8VeseckyJakub.png")
IIIB8ZidkovaLinda = img("faces/IIIB8ZidkovaLinda.png")
IVA8BouchalMarek = img("faces/IVA8BouchalMarek.png")
IVA8BrozdaAdam = img("faces/IVA8BrozdaAdam.png")
IVA8CanibalFilip = img("faces/IVA8CanibalFilip.png")
IVA8CoufalovaJudita = img("faces/IVA8CoufalovaJudita.png")
IVA8DvorskyMichal = img("faces/IVA8DvorskyMichal.png")
IVA8GeprtovaMartina = img("faces/IVA8GeprtovaMartina.png")
IVA8HalasVaclav = img("faces/IVA8HalasVaclav.png")
IVA8JuraMarek = img("faces/IVA8JuraMarek.png")
IVA8KaresVit = img("faces/IVA8KaresVit.png")
IVA8KlimcakovaAnna = img("faces/IVA8KlimcakovaAnna.png")
IVA8KoupilFlorian = img("faces/IVA8KoupilFlorian.png")
IVA8KovarikVojtech = img("faces/IVA8KovarikVojtech.png")
IVA8KurfurstAdam = img("faces/IVA8KurfurstAdam.png")
IVA8LosseovaMarie = img("faces/IVA8LosseovaMarie.png")
IVA8MohaplTomas = img("faces/IVA8MohaplTomas.png")
IVA8NavratilovaAmelie = img("faces/IVA8NavratilovaAmelie.png")
IVA8NiemiecJiri = img("faces/IVA8NiemiecJiri.png")
IVA8PippalNikolas = img("faces/IVA8PippalNikolas.png")
IVA8PospisilovaAnezka = img("faces/IVA8PospisilovaAnezka.png")
IVA8ProchazkaJosef = img("faces/IVA8ProchazkaJosef.png")
IVA8ProchazkovaAnezka = img("faces/IVA8ProchazkovaAnezka.png")
IVA8PuskasJSamuel = img("faces/IVA8PuskasJSamuel.png")
IVA8SrotovaLucie = img("faces/IVA8SrotovaLucie.png")
IVA8VanekKarel = img("faces/IVA8VanekKarel.png")
IVA8VortelJakub = img("faces/IVA8VortelJakub.png")
IVA8ZimovaSKarolina = img("faces/IVA8ZimovaSKarolina.png")
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
known_face_encodings = [AbrahamovaTv, Adamikova2AjRuD, BednarikovaMaITV, BerankovaAjFr, BraunerChBi, CastellarSp, CechovaAj, ChromaTvZ, DanielTvZ, DohnalovaCjHv, DostalovaTv, DubovaNeCj, DvorskyAjD, FaberovaAjRu, FerencMaFy, FukaCjNe, GlosCjD, HajduMaAj, HajekBiCh, HamrikovaMaCh, HavranovaAj, HermanovaCjHvRu, HorvathSp, HubackovaCjD, IA8AuxtovaLinda, IA8BartosJan, IA8BenesovaJohana, IA8BouchalovaKveta, IA8ChmelovaVendula, IA8CisarVojtech, IA8DostalJakub, IA8FilousovaAlzbeta, IA8GajdusekMiroslav, IA8GogolJMatyas, IA8GrassovaEla, IA8HalatovaVeronika, IA8HandlovaKaterina, IA8HarnosovaAlzbeta, IA8HulikovaAmelie, IA8IlleovaAdela, IA8JensDavid, IA8KmentovaMarie, IA8KornhonTomas, IA8KropacDavid, IA8LonicekMartin, IA8MaslikovaKarolina, IA8MohylovaLaura, IA8MuchovaJohana, IA8NavratilDaniel, IA8ProchazkaJan, IA8StefanuttovaAmalie, IA8SterbovaSDana, IA8TichyMaxmilian, IA8ZdrazilovaAKarolina, IB8BrundaMikulas, IB8BurdaJan, IB8ChrasteckyJan, IB8DoubalovaJarmila, IB8FischerOndrej, IB8GastaPetr, IB8IloemezueBeaAdachi, IB8KlimcakRichard, IB8KonecnaElla, IB8KubickovaSofire, IB8KubikJachym, IB8LacovaKristina, IB8LinekOndrej, IB8MachacovaEdita, IB8MorbicrovaAdela, IB8NgoTuongVan, IB8OndrouskovaTereza, IB8OpavskyVit, IB8PeterovaMichaela, IB8PiechDaniel, IB8RaabovaIva, IB8StoppenovaJulie, IB8TisovskyMikulas, IB8UtikalovaNJustyna, IB8VelickyVaclav, IB8VodickovaKristyna, IB8ZavadilTomas, IB8ZdarilDaniel, IIA8BalnerJakub, IIA8CablikovaAnna, IIA8CernaStella, IIA8CoufalovaBerenika, IIA8DupalovaMichaela, IIA8HajekKrystof, IIA8HamplJonas, IIA8HebelkaEdward, IIA8HyzlovaKaterina, IIA8KrumniklMartin, IIA8KuceraMiroslav, IIA8LokocMartin, IIA8MisurcovaMarie, IIA8OklestkovaZuzana, IIA8PerneckaAnna, IIA8PilkovaMagdalena, IIA8PospisilovaAnna, IIA8ProtivanekVojtech, IIA8SasinkaJaromir, IIA8SeckarovaVeronika, IIA8SlukaOndrej, IIA8SmerekFrantisek, IIA8SrovnalikovaSofie, IIA8TomankovaMahulena, IIA8UlicnyTOldrich, IIA8VaclavikovaAnna, IIA8VevodovaSofie, IIA8ZubakSamuel, IIIA8BazantovaMagdalena, IIIA8BlahutovaEKarolina, IIIA8BodnarovaEma, IIIA8BubenicekDavid, IIIA8DejlMartin, IIIA8DrozdovaNela, IIIA8DudaBenjamin, IIIA8DvorakovaTereza, IIIA8FiserovaJana, IIIA8HoangovaAnh, IIIA8HolasekTomas, IIIA8HorakAlexandr, IIIA8HrabalNikola, IIIA8JanosikLukas, IIIA8KralovaIvana, IIIA8KratkyLukas, IIIA8KubikovaEliska, IIIA8KudlaRudolf, IIIA8KvapilovaTereza, IIIA8MutinaMarek, IIIA8MyskovaTereza, IIIA8NovakovaDaniela, IIIA8SlezarovaAnna, IIIA8SmekalovaLucie, IIIA8StavarskyRichard, IIIA8ValentovaVeronika, IIIA8VohralikovaJohana, IIIA8ZikmundovaAdela, IIIB8AmbrosMichael, IIIB8AxmanovaPavlina, IIIB8BuresEBenjamin, IIIB8CoufalovaNoemi, IIIB8DolezalovaHelena, IIIB8HavrlantSimon, IIIB8HimrJonas, IIIB8HockadaySMatthew, IIIB8HoudekJan, IIIB8JuraskovaAneta, IIIB8KlimkovaViola, IIIB8KolarJan, IIIB8KonecnyPetr, IIIB8LazarovaSofie, IIIB8MadrovaGabriela, IIIB8PaulickovaTereza, IIIB8PetrivalskyNil, IIIB8PolednovaSofie, IIIB8RatajovaTerezie, IIIB8SaradinMatej, IIIB8SimackovaMEmma, IIIB8SitovaHana, IIIB8SmutnaHana, IIIB8StefanovaAnna, IIIB8StyblovaTatiana, IIIB8TomeckovaAnna, IIIB8VaclavikovaAnna, IIIB8VeseckyJakub, IIIB8ZidkovaLinda, IVA8BouchalMarek, IVA8BrozdaAdam, IVA8CanibalFilip, IVA8CoufalovaJudita, IVA8DvorskyMichal, IVA8GeprtovaMartina, IVA8HalasVaclav, IVA8JuraMarek, IVA8KaresVit, IVA8KlimcakovaAnna, IVA8KoupilFlorian, IVA8KovarikVojtech, IVA8KurfurstAdam, IVA8LosseovaMarie, IVA8MohaplTomas, IVA8NavratilovaAmelie, IVA8NiemiecJiri, IVA8PippalNikolas, IVA8PospisilovaAnezka, IVA8ProchazkaJosef, IVA8ProchazkovaAnezka, IVA8PuskasJSamuel, IVA8SrotovaLucie, IVA8VanekKarel, IVA8VortelJakub, IVA8ZimovaSKarolina, JanickovaAjCj, JonesAj, JurikTvZ, KalandrovaCjOv, KnapekAjSp, KonecnaNeCj, KostkovaMaCh, KovarovaMaCh, KralovaAj, KrcovaMaZ, KrejcirovaSp, KrejcirTvZ, KrizovaMaFy, KvapilMaFyHv, LekesovaCjHv, LetakovaBiCh, MadrovaAj, MarkovaBiCh, MartinikovaNeHv, MasnyOvVv, McMullinAj, MenouskovaCjFr, MinarikMa, NavratilBiZ, NavratilovaAj, NezvalovaAjRuD, OndrakOvLat, PazderovaMaFy, PetrMaFy, PiechovaAj, PohanelMaZAjProjekty, PolednovaMaZ, PridalovaAjRu, PrzybylovaCjHv, PuskarovaNeCj, RehulkaBiCh, RichterkovaMaFy, SedlackovaCjFr, SeverovaMaIVT, SladecekCjAj, SoubustovaNeRu, StanecSp, StepanovIVT, StranskaFy, StudnickaMaIVT, SuchankovaAj, SykorovaAjD, TeplyAjTv, UrbaskovaMaZ, VackovaCjVVEkonomie, VasiljevovaBiVV, VavraCjVV, VeselaCjNe, VitamvasovaAj, VojtovicovaMaFyAj, ZabojovaBiCh, ZajicovaCjNe, ZarubovaMaCh, ZatloukalovaVVRu]
known_face_names = ['AbrahamovaTv', 'Adamikova2AjRuD', 'BednarikovaMaITV', 'BerankovaAjFr', 'BraunerChBi', 'CastellarSp', 'CechovaAj', 'ChromaTvZ', 'DanielTvZ', 'DohnalovaCjHv', 'DostalovaTv', 'DubovaNeCj', 'DvorskyAjD', 'FaberovaAjRu', 'FerencMaFy', 'FukaCjNe', 'GlosCjD', 'HajduMaAj', 'HajekBiCh', 'HamrikovaMaCh', 'HavranovaAj', 'HermanovaCjHvRu', 'HorvathSp', 'HubackovaCjD', 'IA8AuxtovaLinda', 'IA8BartosJan', 'IA8BenesovaJohana', 'IA8BouchalovaKveta', 'IA8ChmelovaVendula', 'IA8CisarVojtech', 'IA8DostalJakub', 'IA8FilousovaAlzbeta', 'IA8GajdusekMiroslav', 'IA8GogolJMatyas', 'IA8GrassovaEla', 'IA8HalatovaVeronika', 'IA8HandlovaKaterina', 'IA8HarnosovaAlzbeta', 'IA8HulikovaAmelie', 'IA8IlleovaAdela', 'IA8JensDavid', 'IA8KmentovaMarie', 'IA8KornhonTomas', 'IA8KropacDavid', 'IA8LonicekMartin', 'IA8MaslikovaKarolina', 'IA8MohylovaLaura', 'IA8MuchovaJohana', 'IA8NavratilDaniel', 'IA8ProchazkaJan', 'IA8StefanuttovaAmalie', 'IA8SterbovaSDana', 'IA8TichyMaxmilian', 'IA8ZdrazilovaAKarolina', 'IB8BrundaMikulas', 'IB8BurdaJan', 'IB8ChrasteckyJan', 'IB8DoubalovaJarmila', 'IB8FischerOndrej', 'IB8GastaPetr', 'IB8IloemezueBeaAdachi', 'IB8KlimcakRichard', 'IB8KonecnaElla', 'IB8KubickovaSofire', 'IB8KubikJachym', 'IB8LacovaKristina', 'IB8LinekOndrej', 'IB8MachacovaEdita', 'IB8MorbicrovaAdela', 'IB8NgoTuongVan', 'IB8OndrouskovaTereza', 'IB8OpavskyVit', 'IB8PeterovaMichaela', 'IB8PiechDaniel', 'IB8RaabovaIva', 'IB8StoppenovaJulie', 'IB8TisovskyMikulas', 'IB8UtikalovaNJustyna', 'IB8VelickyVaclav', 'IB8VodickovaKristyna', 'IB8ZavadilTomas', 'IB8ZdarilDaniel', 'IIA8BalnerJakub', 'IIA8CablikovaAnna', 'IIA8CernaStella', 'IIA8CoufalovaBerenika', 'IIA8DupalovaMichaela', 'IIA8HajekKrystof', 'IIA8HamplJonas', 'IIA8HebelkaEdward', 'IIA8HyzlovaKaterina', 'IIA8KrumniklMartin', 'IIA8KuceraMiroslav', 'IIA8LokocMartin', 'IIA8MisurcovaMarie', 'IIA8OklestkovaZuzana', 'IIA8PerneckaAnna', 'IIA8PilkovaMagdalena', 'IIA8PospisilovaAnna', 'IIA8ProtivanekVojtech', 'IIA8SasinkaJaromir', 'IIA8SeckarovaVeronika', 'IIA8SlukaOndrej', 'IIA8SmerekFrantisek', 'IIA8SrovnalikovaSofie', 'IIA8TomankovaMahulena', 'IIA8UlicnyTOldrich', 'IIA8VaclavikovaAnna', 'IIA8VevodovaSofie', 'IIA8ZubakSamuel', 'IIIA8BazantovaMagdalena', 'IIIA8BlahutovaEKarolina', 'IIIA8BodnarovaEma', 'IIIA8BubenicekDavid', 'IIIA8DejlMartin', 'IIIA8DrozdovaNela', 'IIIA8DudaBenjamin', 'IIIA8DvorakovaTereza', 'IIIA8FiserovaJana', 'IIIA8HoangovaAnh', 'IIIA8HolasekTomas', 'IIIA8HorakAlexandr', 'IIIA8HrabalNikola', 'IIIA8JanosikLukas', 'IIIA8KralovaIvana', 'IIIA8KratkyLukas', 'IIIA8KubikovaEliska', 'IIIA8KudlaRudolf', 'IIIA8KvapilovaTereza', 'IIIA8MutinaMarek', 'IIIA8MyskovaTereza', 'IIIA8NovakovaDaniela', 'IIIA8SlezarovaAnna', 'IIIA8SmekalovaLucie', 'IIIA8StavarskyRichard', 'IIIA8ValentovaVeronika', 'IIIA8VohralikovaJohana', 'IIIA8ZikmundovaAdela', 'IIIB8AmbrosMichael', 'IIIB8AxmanovaPavlina', 'IIIB8BuresEBenjamin', 'IIIB8CoufalovaNoemi', 'IIIB8DolezalovaHelena', 'IIIB8HavrlantSimon', 'IIIB8HimrJonas', 'IIIB8HockadaySMatthew', 'IIIB8HoudekJan', 'IIIB8JuraskovaAneta', 'IIIB8KlimkovaViola', 'IIIB8KolarJan', 'IIIB8KonecnyPetr', 'IIIB8LazarovaSofie', 'IIIB8MadrovaGabriela', 'IIIB8PaulickovaTereza', 'IIIB8PetrivalskyNil', 'IIIB8PolednovaSofie', 'IIIB8RatajovaTerezie', 'IIIB8SaradinMatej', 'IIIB8SimackovaMEmma', 'IIIB8SitovaHana', 'IIIB8SmutnaHana', 'IIIB8StefanovaAnna', 'IIIB8StyblovaTatiana', 'IIIB8TomeckovaAnna', 'IIIB8VaclavikovaAnna', 'IIIB8VeseckyJakub', 'IIIB8ZidkovaLinda', 'IVA8BouchalMarek', 'IVA8BrozdaAdam', 'IVA8CanibalFilip', 'IVA8CoufalovaJudita', 'IVA8DvorskyMichal', 'IVA8GeprtovaMartina', 'IVA8HalasVaclav', 'IVA8JuraMarek', 'IVA8KaresVit', 'IVA8KlimcakovaAnna', 'IVA8KoupilFlorian', 'IVA8KovarikVojtech', 'IVA8KurfurstAdam', 'IVA8LosseovaMarie', 'IVA8MohaplTomas', 'IVA8NavratilovaAmelie', 'IVA8NiemiecJiri', 'IVA8PippalNikolas', 'IVA8PospisilovaAnezka', 'IVA8ProchazkaJosef', 'IVA8ProchazkovaAnezka', 'IVA8PuskasJSamuel', 'IVA8SrotovaLucie', 'IVA8VanekKarel', 'IVA8VortelJakub', 'IVA8ZimovaSKarolina', 'JanickovaAjCj', 'JonesAj', 'JurikTvZ', 'KalandrovaCjOv', 'KnapekAjSp', 'KonecnaNeCj', 'KostkovaMaCh', 'KovarovaMaCh', 'KralovaAj', 'KrcovaMaZ', 'KrejcirovaSp', 'KrejcirTvZ', 'KrizovaMaFy', 'KvapilMaFyHv', 'LekesovaCjHv', 'LetakovaBiCh', 'MadrovaAj', 'MarkovaBiCh', 'MartinikovaNeHv', 'MasnyOvVv', 'McMullinAj', 'MenouskovaCjFr', 'MinarikMa', 'NavratilBiZ', 'NavratilovaAj', 'NezvalovaAjRuD', 'OndrakOvLat', 'PazderovaMaFy', 'PetrMaFy', 'PiechovaAj', 'PohanelMaZAjProjekty', 'PolednovaMaZ', 'PridalovaAjRu', 'PrzybylovaCjHv', 'PuskarovaNeCj', 'RehulkaBiCh', 'RichterkovaMaFy', 'SedlackovaCjFr', 'SeverovaMaIVT', 'SladecekCjAj', 'SoubustovaNeRu', 'StanecSp', 'StepanovIVT', 'StranskaFy', 'StudnickaMaIVT', 'SuchankovaAj', 'SykorovaAjD', 'TeplyAjTv', 'UrbaskovaMaZ', 'VackovaCjVVEkonomie', 'VasiljevovaBiVV', 'VavraCjVV', 'VeselaCjNe', 'VitamvasovaAj', 'VojtovicovaMaFyAj', 'ZabojovaBiCh', 'ZajicovaCjNe', 'ZarubovaMaCh', 'ZatloukalovaVVRu']


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
 