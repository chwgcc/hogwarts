# -*- coding: utf-8 -*-
# @Time     : 2020/12/6 9:53
# @Author   : chw
# @File     : test_1.py

curl -s 'https://xueqiu.com/stock/search.json?code=sougou&size=3&page=1' \
  -H 'Connection: keep-alive' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36' \
  -H 'elastic-apm-traceparent: 00-a8710b17454e3b694c62175689847e08-a117ec555f47b270-00' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Referer: https://xueqiu.com/k?q=sougou' \
  -H 'Accept-Language: zh-CN,zh;q=0.9' \
  -H 'Cookie: acw_tc=2760822f16072178178472029e8c22a5bb951a6efc76d024bdf493b52a9e9f; xq_a_token=1132205e8c57eb587b26526804cff9f3b6bf6799; xqat=1132205e8c57eb587b26526804cff9f3b6bf6799; xq_r_token=81b9c911ea3907729d8f8e9f60d9f5251227c551; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTYwOTEyMzA1NywiY3RtIjoxNjA3MjE3ODA3OTM2LCJjaWQiOiJkOWQwbjRBWnVwIn0.iTLahqy6ncL3Ium2hua3VXIBuMHPnj0lyMlvMemg6sWgr6oD_0BS-Mz7iqH07zjrGtrixGgBSZFHwhwRjxqePjJHTIm-iQF4HonDfNzUQqY9UupBy1K_wHQWY3IK8PrW3MagbA5W70GCF3rrxBg1fr7QTigBb8wDO8JvNvtadTBriE0dfwkJuN7ItVDv1GU2ZNT215S7SByEKvBDS0jMaua3a3Khg4LmhMmS6Yq7q1phtR5fsLpWUGWfmzNOZ7ZYjHplslgEZXfLxofA97y4ElYt6lH1KPGQHH4ZTi55ihSnNEgIzGx-Y4rm0sdPAi5jMuJ_KpwFb2_EnDJulk_tzQ; u=361607217817856; device_id=24700f9f1986800ab4fcc880530dd0ed; Hm_lvt_1db88642e346389874251b5a1eded6e3=1607217803; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1607217823' \
  --compressed