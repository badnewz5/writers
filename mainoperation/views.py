from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    category=Category.objects.get(category_name='living')
    new_arrival = Product.objects.all().order_by('-id')[:3]
    living_products = Product.objects.filter(category=category).order_by('-id')[:4]
    popular_category=Category.objects.all().order_by('id')[:8]
    return render(request, "mainoperation/index.html",{'new_arrival':new_arrival,'living_products':living_products,'popular_category':popular_category})


def living(request):
    category=Category.objects.get(category_name='living')
    living_products = Product.objects.all().order_by('id')[:9]
    return render(request, "Living/Living.html",{'living_products':living_products})



def dining(request):
    category = Category.objects.get(category_name="dining")
    dining_products = Product.objects.all().order_by('id')[:9]
    return render(request, "Dining/dining.html",{'dining_products':dining_products})


def decoration(request):
    category=Category.objects.get(category_name='decoration')
    decoration_products = Product.objects.all().order_by('id')[:9]
    return render(request, "Decoration/decoration.html",{'decoration_products':decoration_products})


def office(request):
    category = Category.objects.get(category_name="office furniture")
    office_products = Product.objects.all().order_by('id')[:9]
    return render(request, "Office/office.html",{'office_products':office_products})


def rugs(request):
    new_arrival = Product.objects.filter()
    category=Category.objects.get(category_name='rugs and textiles')
    rugs_products  = Product.objects.all().order_by('id')[:9]
    return render(request, "Rugs/rugs.html",{'rugs_products':rugs_products})


def beedroom(request):
    category=Category.objects.get(category_name='beed room')
    beedroom_products = Product.objects.all().order_by('id')[:9]
    return render(request, "BeedRoom/beedroom.html",{'beedroom_products':beedroom_products})


def kitchen(request):
    category=Category.objects.get(category_name="kitchen furniture")
    kitchen_products = Product.objects.all().order_by('id')[:9]
    office_products = Product.objects.filter()
    return render(request, "Kitchen/kitchen.html",{'kitchen_products':kitchen_products})


def otheritem(request):
    category=Category.objects.get(category_name='other item')
    otheritem_products = Product.objects.all().order_by('id')[:9]
    return render(request, "OtherItem/otheritem.html",{'otheritem_products':otheritem_products })


def promotion(request):
    category=Category.objects.get(category_name='promotion')
    promotion_products =Promotion.objects.all()
    return render(request, "Promotion/promotion.html",{'promotion_products':promotion_products})


def coffetable(request):
    coffetable_products = Product.objects.filter(name="Coffee table" )
    office_products = Product.objects.filter()
    return render(request, "Living/coffetable.html",{'coffetable_products': coffetable_products})


def bars(request):
    bars_products = Product.objects.filter(name="Bars")
    office_products = Product.objects.filter()
    return render(request, "Living/bars.html",{'bars_products':bars_products})


def chair(request):
    chair_products = Product.objects.filter(name="chairs")
    office_products = Product.objects.filter()
    return render(request, "Living/chair.html",{'chair_products':chair_products})


def console(request):
    console_products = Product.objects.filter(name="Console")
    office_products = Product.objects.filter()
    return render(request, "Living/console.html",{'console_products':console_products})


def livingroom(request):
    livingroom_products = Product.objects.filter(name='livingroom')
    office_products = Product.objects.filter()
    return render(request, "Living/livingroom.html",{'livingroom_products':livingroom_products})


def mirrors(request):
    mirrors_products = Product.objects.filter(name="mirrors")
    office_products = Product.objects.filter()
    return render(request, "Living/mirrors.html",{'mirrors_products':mirrors_products})


def sofabed(request):
    sofabed_products = Product.objects.filter(name="sofabed")
    office_products = Product.objects.filter()
    return render(request, "Living/sofabed.html",{'sofabed_products': sofabed_products})


def sofa(request):
    sofa_products = Product.objects.filter(name="sofa")
    office_products =Product.objects.filter()
    return render(request, "Living/sofa.html",{'sofa_products':sofa_products})


def tvmedia(request):
    tvmedia_products = Product.objects.filter(name="tvmedia")
    office_products = Product.objects.filter()
    return render(request, "Living/tvmedia.html",{'tvmedia_products':tvmedia_products })


def delivery(request):
    new_arrival = Product.objects.filter()
    delivery_products = Product.objects.filter(category__category_name='delivery')
    office_products = Product.objects.filter()
    return render(request, "Delivery/delivery.html")


def buffet(request):
    new_arrival = Product.objects.filter()
    buffet_products = Product.objects.filter(name="buffet")
    office_products = Product.objects.filter()
    return render(request, "Dining/buffet.html",{'buffet_products':buffet_products})


def diningchair(request):
    diningchair_products = Product.objects.filter(name="diningchair")
    return render(request, "Dining/diningchair.html",{'diningchair_products':diningchair_products})


def diningseat(request):
    diningseat_products = Product.objects.filter(name="diningset")
    office_products = Product.objects.filter()
    return render(request, "Dining/diningseat.html",{'diningseat_products':diningseat_products})


def desktable(request):
    desktable_products = Product.objects.filter(name="desktable")
    office_products = Product.objects.filter()
    return render(request, "Office/desktable.html",{'desktable_products':desktable_products})


def officechair(request):
    officechair_products = Product.objects.filter(name="officechair")
    office_products = Product.objects.filter()
    return render(request, "Office/officechair.html",{'officechair_products':officechair_products})


def officesofa(request):
    officesofa_products = Product.objects.filter(name="officesofa")
    office_products = Product.objects.filter()
    return render(request, "Office/officesofa.html",{'officesofa_products':officesofa_products })


def sofas(request):
    new_arrival = Product.objects.filter()
    sofas_products = Product.objects.filter(name="safes")
    office_products = Product.objects.filter()
    return render(request, "Office/sofas.html",{'sofas_products':sofas_products})


def officestationary(request):
    new_arrival = Product.objects.filter()
    officestationary_products = Product.objects.filter(name="officestationary")
    office_products = Product.objects.filter()
    return render(request, "Office/officestationary.html",{'officestationary_products':officestationary_products})


def candle(request):
    new_arrival = Product.objects.filter()
    candle_products = Product.objects.filter(name="candle")
    office_products = Product.objects.filter()
    return render(request, "Decoration/candle.html",{'candle_products':candle_products })


def homedecoration(request):
    new_arrival = Product.objects.filter()
    homedecoration_products = Product.objects.filter(name="homedecoration")
    office_products = Product.objects.filter()
    return render(request, "Decoration/homedecoration.html",{'homedecoration_products':homedecoration_products})


def menuitem(request):
    new_arrival = Product.objects.filter()
    menuitem_products = Product.objects.filter(name="menuitem")
    office_products = Product.objects.filter()
    return render(request, "Decoration/menuitem.html",{'menuitem_products':menuitem_products})


def homeaccessories(request):
    new_arrival = Product.objects.filter()
    homeaccessories_products = Product.objects.filter(name="homeaccessories")
    office_products = Product.objects.filter()
    return render(request, "Decoration/homeaccessories.html",{'homeaccessories_products':homeaccessories_products})


def beedroomset(request):
    beedroomset_products = Product.objects.filter(name="beedroomset")
    office_products = Product.objects.filter()
    return render(request, "BeedRoom/beedroomset.html",{'beedroomset_products':beedroomset_products})


def childrenbeedroom(request):
    childrenbeedroom_products = Product.objects.filter(name="childrenbeedroom")
    office_products = Product.objects.filter()
    return render(request, "BeedRoom/childrenbeedroom.html",{'childrenbeedroom_products':childrenbeedroom_products})


def wardrobe(request):
    wardrobe_products = Product.objects.filter(name="wardrobe")
    office_products = Product.objects.filter()
    return render(request, "BeedRoom/wardrobe.html",{'wardrobe_products':wardrobe_products})


def kitchenaccessories(request):
    kitchenaccessories_products = Product.objects.filter(name="kitchenaccessories")
    office_products = Product.objects.filter()
    return render(request, "Kitchen/kitchenaccessories.html",{'kitchenaccessories_products':kitchenaccessories_products})


def kitchenfurniture(request):
    new_arrival = Product.objects.filter()
    kitchenfurniture_products = Product.objects.filter(name="kitchenfurniture")
    office_products = Product.objects.filter()
    return render(request, "Kitchen/kitchenfurniture.html",{'kitchenfurniture_products':kitchenfurniture_products})


def kitchenteacup(request):
    kitchenteacup_products = Product.objects.filter(name="kitchenteacup")
    office_products = Product.objects.filter()
    return render(request, "Kitchen/kitchenteacup.html",{'kitchenteacup_products':kitchenteacup_products})


def kitchenline(request):
    kitchenline_products = Product.objects.filter(name="kitchenline")
    office_products = Product.objects.filter()
    return render(request, "Kitchen/kitchenline.html",{'kitchenline_products':kitchenline_products})


def kitchenelectronics(request):
    kitchenelectronics_products = Product.objects.filter(name="kitchenelectronics")
    office_products = Product.objects.filter()
    return render(request, "Kitchen/kitchenelectronics.html",{'kitchenelectronics_products':kitchenelectronics_products })


def kitchenplastics(request):
    kitchenplastics_products = Product.objects.filter(name="kitchenplastics")
    office_products = Product.objects.filter()
    return render(request, "Kitchen/kitchenplastics.html",{'kitchenplastics_products':kitchenplastics_products })


def lighting(request):
    new_arrival = Product.objects.filter()
    lighting_products = Product.objects.filter(name="lighting")
    office_products = Product.objects.filter()
    return render(request, "OtherItem/lighting.html",{'lighting_products': lighting_products })


def sport(request):
    new_arrival = Product.objects.filter()
    sport_products = Product.objects.filter(name="sport")
    office_products = Product.objects.filter()
    return render(request, "OtherItem/sport.html",{'sport_products':sport_products})


def luandrycleaning(request):
    new_arrival = Product.objects.filter()
    luandrycleaning_products = Product.objects.filter(name="luandrycleaning")
    office_products = Product.objects.filter()
    return render(request, "OtherItem/luandrycleaning.html",{'luandrycleaning_products':luandrycleaning_products})


def children(request):
    new_arrival = Product.objects.filter()
    children_products = Product.objects.filter(name="children")
    office_products = Product.objects.filter()
    return render(request, "OtherItem/children.html",{'children_products':children_products})


def bathroom(request):
    new_arrival = Product.objects.filter()
    bathroom_products = Product.objects.filter(name="bathroom")
    office_products = Product.objects.filter()
    return render(request, "OtherItem/bathroom.html",{'bathroom_products':bathroom_products})


def bedding(request):
    new_arrival = Product.objects.filter()
    bedding_products = Product.objects.filter(name="bedding")
    office_products = Product.objects.filter()
    return render(request, "Rugs/bedding.html",{'bedding_products': bedding_products})


def curtainrail(request):
    new_arrival = Product.objects.filter()
    curtainrail_products = Product.objects.filter(name="curtainrail")
    office_products = Product.objects.filter()
    return render(request, "Rugs/curtainrail.html",{'curtainrail_products':curtainrail_products })


def curtainblinds(request):
    new_arrival = Product.objects.filter()
    curtainblinds_products = Product.objects.filter(name="curtainblinds")
    office_products = Product.objects.filter()
    return render(request, "Rugs/curtainblinds.html",{'curtainblinds_products':curtainblinds_products})


def curtainpillows(request):
    new_arrival = Product.objects.filter()
    curtainpillows_products = Product.objects.filter(name="curtainpillows")
    office_products = Product.objects.filter()
    return render(request, "Rugs/curtainpillows.html",{'curtainpillows_products':curtainpillows_products })


def doormats(request):
    new_arrival = Product.objects.filter()
    living_products = Product.objects.filter(name="doormats")
    office_products = Product.objects.filter()
    return render(request, "Rugs/doormats.html",{'living_products':living_products})


def chairpads(request):
    new_arrival = Product.objects.filter()
    chairpads_products = Product.objects.filter(name="chairpads")
    office_products = Product.objects.filter()
    return render(request, "Rugs/chairpads.html",{'chairpads_products':chairpads_products })


def outdoormattrees(request):
    new_arrival = Product.objects.filter()
    outdoormattrees_products = Product.objects.filter(name="outdoormattress")
    office_products = Product.objects.filter()
    return render(request, "Rugs/outdoormattreess.html",{'outdoormattrees_products':outdoormattrees_products})


def plaids(request):
    new_arrival = Product.objects.filter()
    plaids_products = Product.objects.filter(name="plaids")
    office_products = Product.objects.filter()
    return render(request, "Rugs/plaids.html",{'plaids_products':plaids_products })


def quilts(request):
    new_arrival = Product.objects.filter()
    quilts_products = Product.objects.filter(name="quilts")
    office_products = Product.objects.filter()
    return render(request, "Rugs/quilts.html",{'quilts_products':quilts_products })


def rugstextiles(request):
    new_arrival = Product.objects.filter()
    rugstextiles_products = Product.objects.filter(name="rugstextiles")
    office_products = Product.objects.filter()
    return render(request, "Rugs/rugstextiles.html",{'rugstextiles_products':rugstextiles_products })


def basketboxes(request):
    new_arrival = Product.objects.filter()
    basketboxes_products = Product.objects.filter(name="basketboxes")
    office_products = Product.objects.filter()
    return render(request, "Decoration/basketboxes.html",{'basketboxes_products':basketboxes_products})


def teabacks(request):
    new_arrival = Product.objects.filter()
    teabacks_products = Products.objects.filter(category__category_name='teabacks')
    office_products = Products.objects.filter()
    return render(request, "Rugs/teabacks.html")
def about(request):
    new_arrival = Product.objects.filter()
    about_products = Product.objects.filter(category__category_name='about')
    office_products = Product.objects.filter()
    return render(request, "Pages/about.html")
def contact(request):
    new_arrival = Product.objects.filter()
    contact_products = Product.objects.filter()
    office_products = Product.objects.filter()
    return render(request, "Pages/contact.html")
def sample(request):
    new_arrival = Product.objects.filter()
    living_products = Products.objects.filter()
    office_products = Products.objects.filter()
    return render(request, "Rugs/sample.html")
