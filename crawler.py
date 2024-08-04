import requests
import json
import time
import re
import random
if __name__ == "__main__":
    uids = [23191782,19147010,483417795]
else:
    uids_path = "uids.json"
    uids_json = open(uids_path, "r", encoding="utf-8")
    uids = json.loads(uids_json)
create_table = """
CREATE TABLE IF NOT EXISTS `dyinfo` (
    `uid` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
    `type` varchar(112) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
    `content` varchar(5000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
    `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
    `forward_user` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
    `forward_url` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
    `pub_ts` varchar(40) DEFAULT NULL
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '用户信息'

"""
chars = '0123456789' + 'ABCDE'
def generate_random_string(length):
    return ''.join(random.choice(chars) for _ in range(length))
cookies = {
    "buvid3": "142D350C-4217-9F24-E2DA-E73BDF16415F66158infoc",
    "b_nut": "1721821566",
    "_uuid": "4E841B7F-8EB5-DF72-7A63-5436810699BCC65248infoc",
    "buvid_fp": "7924fae04df3a85b2c0315cbc4393f74",
    "enable_web_push": "DISABLE",
    "header_theme_version": "CLOSE",
    "buvid4": "A61BFEF5-C849-CE07-434B-E195ECA6554B67051-024072411-r4olVqclDfEx%2FmqMa7CNnA%3D%3D",
    "home_feed_column": "5",
    "browser_resolution": "1706-906",
    "SESSDATA": "1ab84db1%2C1737946413%2C35fcd%2A71CjAx5k5vgYbF1dPuk4hKpS9tGuAv4hB2IcVLV-upUCgQJooRwbbvJXzlYWGtlF69jJMSVk1pZzZaZE5QZHpCV3Rfck1UM3NmREFUTHhyVm9NbjF0UGo0V3hiWWFIN2lyQjdiNTlTcjg4ODV5UDJqSElYVkdZblRCSEZvTWlLRk1nVktTbXpNOW5nIIEC",
    "bili_jct": "01310af91e6776a0595d17c3da5f0464",
    "DedeUserID": "283453728",
    "DedeUserID__ckMd5": "9e9e71fbdb5f9fff",
    "CURRENT_FNVAL": "4048",
    "bili_ticket": "eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjI0OTQzNzMsImlhdCI6MTcyMjIzNTExMywicGx0IjotMX0.QdrS6QKW2RV_5wvMMUOx_wfIw9v7G7s0Gfa-FSftCHw",
    "bili_ticket_expires": "1722494313",
    "bp_t_offset_283453728": "960174337413873664",
    "rpdid": "|(JJmYlJ~lYu0J'u~ku)kuYuJ",
    "CURRENT_QUALITY": "80",
    "fingerprint": "7924fae04df3a85b2c0315cbc4393f74",
    "buvid_fp_plain": "undefined",
    "LIVE_BUVID": "AUTO3417218232473140",
    "PVID": "1",
    "hit-dyn-v2": "1",
    "b_lsid": "8CF315F5_19106B52E00",
    "sid": "80b0dqic",
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    "Referer": "https://space.bilibili.com/670762178/dynamic",
    "Origin": "https://space.bilibili.com",
    "Connection": "keep-alive",
    # 'Cookie': "buvid3=142D350C-4217-9F24-E2DA-E73BDF16415F66158infoc; b_nut=1721821566; _uuid=4E841B7F-8EB5-DF72-7A63-5436810699BCC65248infoc; buvid_fp=7924fae04df3a85b2c0315cbc4393f74; enable_web_push=DISABLE; header_theme_version=CLOSE; buvid4=A61BFEF5-C849-CE07-434B-E195ECA6554B67051-024072411-r4olVqclDfEx%2FmqMa7CNnA%3D%3D; home_feed_column=5; browser_resolution=1706-906; SESSDATA=1ab84db1%2C1737946413%2C35fcd%2A71CjAx5k5vgYbF1dPuk4hKpS9tGuAv4hB2IcVLV-upUCgQJooRwbbvJXzlYWGtlF69jJMSVk1pZzZaZE5QZHpCV3Rfck1UM3NmREFUTHhyVm9NbjF0UGo0V3hiWWFIN2lyQjdiNTlTcjg4ODV5UDJqSElYVkdZblRCSEZvTWlLRk1nVktTbXpNOW5nIIEC; bili_jct=01310af91e6776a0595d17c3da5f0464; DedeUserID=283453728; DedeUserID__ckMd5=9e9e71fbdb5f9fff; CURRENT_FNVAL=4048; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjI0OTQzNzMsImlhdCI6MTcyMjIzNTExMywicGx0IjotMX0.QdrS6QKW2RV_5wvMMUOx_wfIw9v7G7s0Gfa-FSftCHw; bili_ticket_expires=1722494313; bp_t_offset_283453728=960174337413873664; rpdid=|(JJmYlJ~lYu0J'u~ku)kuYuJ; CURRENT_QUALITY=80; fingerprint=7924fae04df3a85b2c0315cbc4393f74; buvid_fp_plain=undefined; LIVE_BUVID=AUTO3417218232473140; PVID=1; hit-dyn-v2=1; b_lsid=8CF315F5_19106B52E00; sid=80b0dqic",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "Priority": "u=4",
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    "offset": "",
    "host_mid": "",
    "timezone_offset": "-480",
    "platform": "web",
    "features": "itemOpusStyle,listOnlyfans,opusBigCover,onlyfansVote,decorationCard,forwardListHidden,ugcDelete",
    "web_location": "333.999",
    "dm_img_list": "[]",
    "dm_img_str": "V2ViR0wgMS",
    "dm_cover_img_str": "QU5HTEUgKEludGVsLCBJbnRlbChSKSBIRCBHcmFwaGljcyBEaXJlY3QzRDExIHZzXzVfMCBwc181XzApLCBvciBzaW1pbGFyR29vZ2xlIEluYy4gKEludGVsKQ",
    "dm_img_inter": "%7B%22ds%22:[%7B%22t%22:2,%22c%22:%22Y2xlYXJmaXggZy1zZWFyY2ggc2VhcmNoLWNvbnRhaW5lcg%22,%22p%22:[2063,79,536],%22s%22:[503,965,1422]%7D],%22wh%22:[5533,6021,103],%22of%22:[101,202,101]%7D",
    "x-bili-device-req-json": "%7B%22platform%22:%22web%22,%22device%22:%22pc%22%7D",
    "x-bili-web-req-json": "%7B%22spm_id%22:%22333.999%22%7D",
    "w_rid": "",
    "wts": int(time.time()),
}

params["w_rid"] =generate_random_string(32)
def get_item_info(item: dict) -> dict:
    match item["type"]:
        case "DYNAMIC_TYPE_FORWARD":
            tmp = {
                    "type": "动态转发",
                    "content": item["modules"]["module_dynamic"]["desc"]["text"],
                    "forward_user": item["orig"]["modules"]["module_author"]["name"],
                    "pub_ts":item["orig"]["modules"]["module_author"]["pub_ts"],
                }
            try:
                tmp["forward_url"]= item["orig"]["modules"]["module_dynamic"]["major"]["archive"]["jump_url"]
            except KeyError:
                try:
                    tmp["forward_url"]=item["orig"]["modules"]["module_dynamic"]["major"]["live"]["jump_url"]
                except KeyError:
                    tmp["forward_url"]=item["orig"]["modules"]["module_dynamic"]["major"]["opus"]["jump_url"]
        case "DYNAMIC_TYPE_AV":
            tmp = {
                "type": "投稿视频",
                "content": item["modules"]["module_dynamic"]["major"]["archive"]["jump_url"],
                "title": item["modules"]["module_dynamic"]["major"]["archive"]["title"],
                "pub_ts":item["modules"]["module_author"]["pub_ts"],
            }
        case "DYNAMIC_TYPE_WORD":
            tmp = {
                "type": "纯文字动态",
                "content": item["modules"]["module_dynamic"]["major"]["opus"][
                    "summary"
                ]["text"],
                "title": item["modules"]["module_dynamic"]["major"]["opus"]["title"],
                "pub_ts":item["modules"]["module_author"]["pub_ts"],
            }
        case "DYNAMIC_TYPE_DRAW":
            tmp = {
                "type": "带图动态",
                "content": [
                    pic["url"]
                    for pic in item["modules"]["module_dynamic"]["major"]["opus"][
                        "pics"
                    ]
                ],
                "title": item["modules"]["module_dynamic"]["major"]["opus"]["title"],
                "text": item["modules"]["module_dynamic"]["major"]["opus"]["summary"][
                    "text"
                ],
                "pub_ts":item["modules"]["module_author"]["pub_ts"],
            }
        case "DYNAMIC_TYPE_LIVE_RCMD":
            tmp ={
                "type": "直播间开播",
                "content": re.search((item["modules"]["module_dynamic"]["major"]["live_rcmd"]["content"]),r'"link":"//(.*)",'),
                "title": re.search((item["modules"]["module_dynamic"]["major"]["live_rcmd"]["content"]),r'"title":"//(.*)",'),
                "pub_ts":item["modules"]["module_author"]["pub_ts"],
            }
        case _:
            print(item["type"])
            tmp = {"type": "UNKONWN", "content": item["type"]}
            
    return tmp
results = []
for uid in uids:
    params["host_mid"] = str(uid)
    response = requests.get(
        "https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/space",
        params=params,
        cookies=cookies,
        headers=headers,
    )
    resp_json = response.json()
    for item in resp_json["data"]["items"]:
        res = get_item_info(item)
        results.append(res)
print(results)