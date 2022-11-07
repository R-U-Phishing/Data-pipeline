import asyncio
import aiohttp
import requests
from timeit import default_timer as dt
from tqdm import tqdm
import time
import pandas as pd
s = dt()
data = []
phishing = pd.read_csv('/home/ec2-user/workspace/DP/source/online-valid.csv')
phishing = phishing[:1000]

async def fetch(url):
    try:
        tld = get_tld(url, as_object=True)
        return tld.domain
    except:
        return url



async def main():
    futures = [asyncio.ensure_future(fetch(url)) for url in phishing['url']]
    result = await asyncio.gather(*futures)
    phishing["domain"] = result

loop = asyncio.new_event_loop()
loop.run_until_complete(main())
loop.close()

async def get_health(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data.append(response.status)
    except:
        data.append(0)



loop = asyncio.get_event_loop()
loop.run_until_complete(
    asyncio.gather(
        *(get_health(i) for i in tqdm(phishing['url']))
    )
)


print(data)
phishing["status"] = data
phishing = phishing[phishing['status'] == 200]
phishing['label'] = -1
data = phishing[["url", "label"]]
data.to_csv("/home/ec2-user/workspace/DP/source/data.csv", index=False)

print(dt()-s)
