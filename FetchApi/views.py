from django.shortcuts import render
# API client library
import googleapiclient.discovery
from .models import Videos
from django.core.paginator import Paginator
from .filters import video_filter


# API information
api_service_name = "youtube"
api_version = "v3"
# API key
DEVELOPER_KEY = ["AIzaSyD-jKSFEX-7gUop4m1JVa4AXKy2-5GmZPU", "AIzaSyBrOKmIJyfA_3VTanJV5rongZFWwPG5WeM", "AIzaSyAbX1J6GWfg9A9Sx3BF4Fbu26_chktGkXM", "AIzaSyCvuHimzqmF7Jwb43JjjTSaP-1rL_T_pfs"]


# Create your views here.
def home(request):
    return render(request, "index.html")

# Created this function to fetch the data and store it
def Get_data(query, max_result, key):
    try:
        youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey = key) # verify youtube api
        
        request = youtube.search().list( 
                part="snippet",
                maxResults=max_result,
                q=query
            )
        # Query execution
        response = request.execute()
        Videos.objects.all().delete() # Empty the database everytime when query is executed
        mx = response["pageInfo"]["resultsPerPage"]
        for i in range(mx): 
            # Store every values from JSON response 
            videoId = response["items"][i]["id"]["videoId"]
            title = response["items"][i]["snippet"]["title"]
            description = response["items"][i]["snippet"]["description"]
            channelTitle = response["items"][i]["snippet"]["channelTitle"]
            publishTime = response["items"][i]["snippet"]["publishTime"]
            thumbnail = response["items"][i]["snippet"]["thumbnails"]["high"]["url"]

            Videos.objects.create(video_id=videoId, title=title, description=description, publishedDateTime=publishTime, channel_title=channelTitle, thumbnail=thumbnail)
        return 0
        
    except:
        return -1

# Created this function to return the result
def Return_result(request):
    if request.method == 'POST': # if requested method is POST then follow thse steps
        query = request.POST.get('query') # get the query and store it
        mex = 40 # maximum results per query
        for i in DEVELOPER_KEY: # If one API key expires then take another one from the list
            x = Get_data(query, mex, i)
            if x == -1:
                continue
            else:
                break
        data = Videos.objects.all().order_by('-publishedDateTime') # Store the sorted data from database in reverse chronological order of publishing dat-time
        videos_filter = video_filter(request.GET, queryset=data) 

        # Pagination
        paginator = Paginator(data, 5) # Show 5 videos (search results) per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # created dictionary (context) for templates
        context = {
        "data":data,
        "page_obj": page_obj,
        "query":query,
        "filter":videos_filter
        }
        return render(request, "result.html", context)

# else if requested method is GET
# filtering according to given input from result.html
    title_s = request.GET.get('title_s')
    description_s = request.GET.get('description_s')
    channel_title_s = request.GET.get('channel_title_s')

    # if any field is not in the query then just replace it with empty string
    if not title_s:
        title_s = ""

    if not description_s:
        description_s = ""

    if not channel_title_s:
        channel_title_s = ""

    # filter the stored data with given search query
    data = Videos.objects.filter(title__contains=title_s, description__contains=description_s, channel_title__contains=channel_title_s).order_by('-publishedDateTime') 

    # Pagination
    paginator = Paginator(data, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "data":data,
        "page_obj": page_obj,
    }
    return render(request, "result.html", context)
