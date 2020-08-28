
def solution(completed, adClicks, alluserips):
    ip_to_address = dict()
    text_dict = dict()
    ans = []
    for id_ip in alluserips:
        print(id_ip)
        id, ip = id_ip.split(',')
        ip_to_address[ip] = id
    for ad in adClicks:
        ip, _, text = ad.split(',')
        text_dict[text] = [0, 0]
        if ip_to_address[ip] in completed:
            text_dict[text][0] += 1
            text_dict[text][1] += 1
        else:
            text_dict[text][1] += 1
    for key, value in text_dict.items():
        ans.append("{} of {} {}".format(value[0], value[1], key))
    return ans


c = ["3123122444", "234111110", "8321125440", "99911063"]
ad_clicks = [
  "122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
  "96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
  "122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
  "82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
  "92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
  "92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens",
]
all_user_ips = [
  "2339985511,122.121.0.155",
  "233998511,122.121.0.250",
  "2342134123,96.3.199.11",
  "234111110,122.121.0.1",
  "3123122444,92.130.6.145",
  "39471289472,2001:0db8:ac10:fe01:0000:0000:0000:0000",
  "8321125440,82.1.106.8",
  "99911063,92.130.6.144"
]

print(solution(c, ad_clicks, all_user_ips))

# O(n), O(n)