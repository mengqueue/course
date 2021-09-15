import time

from django.core.cache import cache
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class HelloMiddle(MiddlewareMixin):
    # def process_request(self, request):
    #     # 打印访问者ip
    #     ip = request.META.get("REMOTE_ADDR")
    #     print(ip)
    #     # 防止过度访问（反爬虫）
    #     # if request.path == "/app/search/":
    #     #     result = cache.get(ip)
    #     #     if result:
    #     #         return HttpResponse("您的访问过于频繁，请10s之后再次检索")
    #     #     cache.set(ip, ip, timeout=10)
    #
    #     # 存放黑名单（cache_key=black）
    #     black_list = cache.get('black', [])
    #
    #     if ip in black_list:
    #         return HttpResponse("您处于黑名单用户中，请联系网站管理员说明情况后方可解除")
    #
    #     requests = cache.get(ip, [])
    #     # 与当前时间相比大于60s的请求被踢出缓存（一分钟之内请求不超过10次）
    #     while requests and time.time()-requests[-1] > 60:
    #         requests.pop()
    #
    #     requests.insert(0, time.time())
    #     cache.set(ip, requests, timeout=60)
    #
    #     if len(requests) > 30:
    #         black_list.append(ip)
    #         cache.set('black', black_list, timeout=60*60*24)
    #         return HttpResponse("小爬虫小黑屋里面呆着吧")
    #
    #     if len(requests) > 10:
    #         return HttpResponse("请求过于频繁，请稍后再试")
        pass