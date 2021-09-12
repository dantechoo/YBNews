from django.shortcuts import render

# Create your views here.
from News import models
import  math
page1 = 1  # current page

def index(request,pageindex=None):
    global page1 # reload and open this page will keep page1 value
    pagesize = 8 # number of data can by display on 1 page
    newsall = models.News_info.objects.all().order_by('-id') # get the data and set the show by shortlist
    datasize = len(newsall) # num of news
    total_page = math.ceil(datasize/pagesize) # total page
    if pageindex == None :  #if no index
        page1 =1
        news_details = models.News_info.objects.filter(enabled = True).order_by('-id')[:pagesize]
    elif pageindex == '1':  #last page
         start = (page1-2)*pagesize #current page 1st data details
         if start >= 0 : # got last page detail/data
             news_details = models.News_info.objects.filter(enabled=True).order_by('-id')[start:(start+pagesize)]
             page1 -= 1 # next page
    elif pageindex == '2': #next page
         start = page1*pagesize # current page 1 data details
         if start < datasize: # next page data is show it
             news_details = models.News_info.objects.filter(enabled = True).order_by('-id')[start:(start+pagesize)]
             page1 += 1
    elif pageindex == '3': #from details page back to main page
         start =(page1-1)*pagesize #load original data by 1st data detail on current page
         news_details = models.News_info.objects.filter(enabled = True).order_by('-id')[start:(start+pagesize)]
    current_page =page1 #loop back to main page value and send to html
    return render(request, 'index.html',locals())

def detail(request, detailid=None):
    unit = models.News_info.objects.get(id=detailid) # load data by detail id
    cate = unit.cat
    title = unit.title
    pub_time = unit.pubtime
    nick_name = unit.name
    message_content = unit.message
    unit.press += 1
    unit.save()

    return render(request, 'detail.html', locals())



