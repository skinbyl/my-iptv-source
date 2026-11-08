import os
import requests

OUTPUT = "output/live.m3u"
channel_list = [
    {"name": "CCTV1 综合", "url": "https://cctv1-hls.cctv.com/cctv1.m3u8"},
    {"name": "CCTV2 财经", "url": "https://cctv2-hls.cctv.com/cctv2.m3u8"},
    {"name": "CCTV3 综艺", "url": "https://cctv3-hls.cctv.com/cctv3.m3u8"},
    {"name": "CCTV4 中文国际", "url": "https://cctv4-hls.cctv.com/cctv4.m3u8"},
    {"name": "CCTV5 体育", "url": "https://cctv5-hls.cctv.com/cctv5.m3u8"},
]

content = "#EXTM3U\n"
for ch in channel_list:
    content += f'#EXTINF:-1,{ch["name"]}\n{ch["url"]}\n'

os.makedirs("output", exist_ok=True)
with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ m3u文件生成完成")
