from flask import Flask, request, jsonify
import sys
import numpy as np
import pickle
import requests
from lxml import html
application = Flask(__name__)

@application.route("/")
@application.route('/home')
def home():
    return "''<h3>안뇽!</h3>''"

url = 'https://finance.naver.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}

@application.route('/exchange', methods=['POST'])
def exchange():
    
    html_req = requests.get(url, headers = headers)
    
    tree = html.fromstring(html_req.text)
    body = tree.xpath('//div[@id ="content"]/div[2]/div/div[1]/table/tbody')[0]

    exchange_name = body.xpath('.//th/a/text()')
    exchange_prices = body.xpath('.//td[1]/text()')
    exchange_updown = body.xpath('.//td[2]/em/span/text()')
    exchange_fluctuation = body.xpath('.//td[2]/text()')
    
    exchange_name_1 = exchange_name[0]
    exchange_prices_1 = exchange_prices[0]
    exchange_updown_1 = exchange_updown[0]
    if exchange_updown_1== "상승":
         exchange_updown_1 = "🔺"
    elif exchange_updown_1=="하락":
         exchange_updown_1="▼"
    else :
          exchange_updown_1="-"
            
    exchange_fluctuation_1 = exchange_fluctuation[0]
    
    exchange_name_2 = exchange_name[1]
    exchange_prices_2 = exchange_prices[1]
    exchange_updown_2 = exchange_updown[1]
    if exchange_updown_2== "상승":
         exchange_updown_2 = "🔺"
    elif exchange_updown_2=="하락":
         exchange_updown_2="▼"
    else :
          exchange_updown_2="-"
            
    exchange_fluctuation_2 = exchange_fluctuation[1]
    
    exchange_name_3 = exchange_name[2]
    exchange_prices_3 = exchange_prices[2]
    exchange_updown_3 = exchange_updown[2]
    if exchange_updown_3== "상승":
         exchange_updown_3 = "🔺"
    elif exchange_updown_3=="하락":
         exchange_updown_3="▼"
    else :
          exchange_updown_3="-"
            
    exchange_fluctuation_3 = exchange_fluctuation[2]
    
    exchange_name_4 = exchange_name[3]
    exchange_prices_4 = exchange_prices[3]
    exchange_updown_4 = exchange_updown[3]
    if exchange_updown_4== "상승":
         exchange_updown_4 = "🔺"
    elif exchange_updown_4=="하락":
         exchange_updown_4="▼"
    else :
          exchange_updown_4="-"
            
    exchange_fluctuation_4 = exchange_fluctuation[3]
    
    dataSend = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "금일 환전 고시 환율을 알려드리겠습니다."
                    }
                },
                {
                    "listCard": {
                        "header": {
                            "title": "현재 환전 고시 환율 입니다."
                        },
                        "items": [
                            {
                                "title": exchange_name_1,
                                "description": "현재가 : "+exchange_prices_1+" / 등락폭 : "+exchange_updown_1+" "+exchange_fluctuation_1,
                                "link": {
                                    "web": "https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_USDKRW"
                                }
                            },
                            {
                                "title": exchange_name_2,
                                "description": "현재가 : "+exchange_prices_2+" / 등락폭 : "+exchange_updown_2+" "+exchange_fluctuation_2,
                                "link": {
                                    "web": "https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_JPYKRW"
                                }
                            },
                            {
                                "title": exchange_name_3,
                                "description": "현재가 : "+exchange_prices_3+" / 등락폭 : "+exchange_updown_3+" "+exchange_fluctuation_3,
                                "link": {
                                    "web": "https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_EURKRW"
                                }
                            },
                            {
                                "title": exchange_name_4,
                                "description": "현재가 : "+exchange_prices_4+" / 등락폭 : "+exchange_updown_4+" "+exchange_fluctuation_4,
                                "link": {
                                    "web": "https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_CNYKRW"
                                }
                            }
                        ],
                        "buttons": [
                            {
                                "label": "자세히 보기",
                                "action": "webLink",
                                "webLinkUrl": "https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"
                            }
                        ]
                    }
                },
                {
                    "simpleText": {
                        "text": "⚠️ 제공되는 정보는 오류 및 지연이 발생될 수 있으므로 유의하시기 바랍니다."
                    }
                }
            ],
    "quickReplies": [
        {
            "messageText": "처음으로",
            "action": "message",
            "label": "처음으로"
        },
        {
            "messageText": "국내증시",
            "action": "message",
            "label": "국내증시"
        },
        {
            "messageText": "해외증시",
            "action": "message",
            "label": "해외증시"
        },
        {
            "messageText": "인기종목",
            "action": "message",
            "label": "인기종목"
        },
        {
            "messageText": "뉴스",
            "action": "message",
            "label": "뉴스"
        },
        {
            "messageText": "현재가",
            "action": "message",
            "label": "현재가"
        }
    ]
        }
    }
    return jsonify(dataSend)



@application.route('/overseas_stock', methods=['POST'])
def overseas_stock():
    
    html_req = requests.get(url, headers = headers)
    
    tree = html.fromstring(html_req.text)
    body = tree.xpath('//*[@id="container"]/div[3]/div/div[1]/table/tbody')[0]

    name = body.xpath('.//th/a/text()')
    prices = body.xpath('.//td[1]/text()')
    updown = body.xpath('.//td[2]/em/span/text()')
    fluctuation = body.xpath('.//td[2]/text()')
    
    name_1 = name[0]
    prices_1 = prices[0]
    updown_1 = updown[0]
    if updown_1== "상승":
         updown_1 = "🔺"
    elif updown_1=="하락":
         updown_1="▼"
    else :
          updown_1="-"
            
    fluctuation_1 = fluctuation[0]
    
    name_2 = name[1]
    prices_2 = prices[1]
    updown_2 = updown[1]
    if updown_2== "상승":
         updown_2 = "🔺"
    elif updown_2=="하락":
         updown_2="▼"
    else :
          updown_2="-"
            
    fluctuation_2 = fluctuation[1]
    
    name_3 = name[2]
    prices_3 = prices[2]
    updown_3 = updown[2]
    if updown_3== "상승":
         updown_3 = "🔺"
    elif updown_3=="하락":
         updown_3="▼"
    else :
          updown_3="-"
            
    fluctuation_3 = fluctuation[2]
    
    name_4 = name[3]
    prices_4 = prices[3]
    updown_4 = updown[3]
    if updown_4== "상승":
         updown_4 = "🔺"
    elif updown_4=="하락":
         updown_4="▼"
    else :
          updown_4="-"
            
    fluctuation_4 = fluctuation[3]
    
    name_5 = name[4]
    prices_5 = prices[4]
    updown_5 = updown[4]
    if updown_5== "상승":
         updown_5 = "🔺"
    elif updown_5=="하락":
         updown_5="▼"
    else :
          updown_5="-"
            
    fluctuation_5 = fluctuation[4]
    
    
    dataSend = {
      "version": "2.0",
      "template": {
        "outputs": [
            {
                "simpleText": {
                    "text": "오늘의 해외증시를 알려드리겠습니다."
                }
            },
          {
            "listCard": {
              "header": {
                "title": "현재 해외증시 입니다."
              },
              "items": [
                {
                  "title": name_1,
                  "description": "현재가 : "+prices_1+" / 등락폭 : "+updown_1+" "+fluctuation_1,
                  "link": {
                    "web": "https://finance.naver.com/world/sise.naver?symbol=DJI@DJI"
                  }
                },
                {
                  "title": name_2,
                  "description": "현재가 : "+prices_2+" / 등락폭 : "+updown_2+" "+fluctuation_2,
                  "link": {
                    "web": "https://finance.naver.com/world/sise.naver?symbol=NAS@IXIC"
                  }
                },
                {
                  "title": name_3,
                  "description": "현재가 : "+prices_3+" / 등락폭 : "+updown_3+" "+fluctuation_3,
                  "link": {
                    "web": "https://m.stock.naver.com/worldstock/index/.HSCE"
                  }
                },
                {
                  "title": name_4,
                  "description": "현재가 : "+prices_4+" / 등락폭 : "+updown_4+" "+fluctuation_4,
                  "link": {
                    "web": "https://m.stock.naver.com/worldstock/index/.SSEC"
                  }
                },
                {
                  "title": name_5,
                  "description": "현재가 : "+prices_5+" / 등락폭 : "+updown_5+" "+fluctuation_5,
                  "link": {
                    "web": "https://m.stock.naver.com/worldstock/index/.N225"
                  }
                }
              ],
              "buttons": [
                {
                  "label": "자세히 보기",
                  "action": "webLink",
                  "webLinkUrl": "https://finance.naver.com/world/"
                }
              ]
            }
          },
            {
                 "simpleText": {
                   "text": "⚠️ 제공되는 정보는 오류 및 지연이 발생될 수 있으므로 유의하시기 바랍니다."
             }
         },
        ],
    "quickReplies": [
        {
        "messageText": "처음으로",
        "action": "message",
        "label": "처음으로"
      },
      {
        "messageText": "국내증시",
        "action": "message",
        "label": "국내증시"
      },
      {
        "messageText": "인기종목",
        "action": "message",
        "label": "인기종목"
      },
      {
        "messageText": "환율",
        "action": "message",
        "label": "환율"
      },
        {
        "messageText": "뉴스",
        "action": "message",
        "label": "뉴스"
          },
        {
         "messageText": "현재가",
         "action": "message",
         "label": "현재가"
        }
        ]

      }
    }
    return jsonify(dataSend)



@application.route('/get_stock_news', methods=['POST'])
def get_stock_news():

    html_req = requests.get(url, headers = headers)

    tree = html.fromstring(html_req.text)
    bodies = tree.xpath('//div[@class ="news_area"]/div[@class="section_strategy"]/ul/li')

    results = []
    for body in bodies:
        news_title = body.xpath('.//span/a/text()')[0]
        try:
             news_url = body.xpath('.//span/a/@href')[0]
        except:
            news_url = ''
        news_title_clean = news_title.replace("\n", "").replace("\t", "").replace("\r", "").strip()
        news_url = 'https://finance.naver.com' + news_url
        results.append([news_title_clean, news_url])
    
    subject_1 = results[0][0]
    news_url_1 = results[0][1]
    print(subject_1)   

    subject_2 = results[1][0]
    news_url_2 = results[1][1]
    print(subject_2) 
    
    subject_3 = results[2][0]
    news_url_3 = results[2][1]
    print(subject_3) 
    
    subject_4 = results[3][0]
    news_url_4 = results[3][1]
    print(subject_4)
    
    subject_5 = results[3][0]
    news_url_5 = results[3][1]
    print(subject_5) 

    dataSend = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                "simpleText": {
                    "text": "오늘의 뉴스를 알려드리겠습니다."
                }
            },
                {
            "listCard": {
              "header": {
                "title": "현재 뉴스 입니다."
              },
              "items": [
                {
                  "title": subject_1,
                  "description": news_url_1,
                  "link": {
                    "web": news_url_1
                  }
                },
                {
                  "title": subject_2,
                  "description": news_url_2,
                  "link": {
                    "web": news_url_2
                  }
                },
                {
                  "title": subject_3,
                  "description": news_url_3,
                  "link": {
                    "web": news_url_3
                  }
                },
                {
                  "title": subject_4,
                  "description": news_url_4,
                  "link": {
                    "web": news_url_4
                  }
                },
                {
                  "title": subject_5,
                  "description": news_url_5,
                  "link": {
                    "web": news_url_5
                  }
                }
              ],
              "buttons": [
                {
                  "label": "자세히 보기",
                  "action": "webLink",
                  "webLinkUrl": "https://finance.naver.com/news/mainnews.naver"
                }
              ]
            }
          },
                {
                 "simpleText": {
                   "text": "⚠️ 제공되는 정보는 오류 및 지연이 발생될 수 있으므로 유의하시기 바랍니다."
             }
         }
        ],
    "quickReplies": [
        {
        "messageText": "처음으로",
        "action": "message",
        "label": "처음으로"
      },
      {
        "messageText": "국내증시",
        "action": "message",
        "label": "국내증시"
      },
      {
        "messageText": "해외증시",
        "action": "message",
        "label": "해외증시"
      },
      {
        "messageText": "인기종목",
        "action": "message",
        "label": "인기종목"
      },
        {
        "messageText": "환율",
        "action": "message",
        "label": "환율"
        },
        {
         "messageText": "현재가",
         "action": "message",
         "label": "현재가"
        }
        ]

      }
    }
    return jsonify(dataSend)



@application.route('/kr_stock', methods = ['POST'])
def kr_stock():
    html_req = requests.get(url, headers = headers)
    
    tree = html.fromstring(html_req.text)
    body = tree.xpath('//div[@class="section_stock"]')[0]
    
    name = body.xpath('.//div/div/h4/a/em/span/text()')
    prices = body.xpath('.//div/div/a/span/span[@class="num"]/text()')
    updown  = body.xpath('.//div/div/a/span/span[@class="num2"]/text()')
    updown_percent_pms = body.xpath('.//div/div/a/span/span[@class="blind"]/text()')
    
    name_1 = name[0]
    prices_1 = prices[0]
    updown_1 = updown[0]
    updown_pm_1 = updown_percent_pms[0]
    if updown_pm_1 == "상승":
         updown_pm_1 = "🔺"
    elif updown_pm_1=="하락":
         updown_pm_1="▼"
    else :
          updown_pm_1="-"
    
    name_2 = name[1]
    prices_2 = prices[1]
    updown_2 = updown[1]
    updown_pm_2 = updown_percent_pms[1]
    if updown_pm_2== "상승":
         updown_pm_2 = "🔺"
    elif updown_pm_2=="하락":
         updown_pm_2="▼"
    else :
          updown_pm_2="-"
    
    name_3 = name[2]
    prices_3 = prices[2]
    updown_3 = updown[2]
    updown_pm_3 = updown_percent_pms[2]
    if updown_pm_3== "상승":
         updown_pm_3 = "🔺"
    elif updown_pm_3=="하락":
         updown_pm_3="▼"
    else :
          updown_pm_3="-"

    dataSend = {
      "version": "2.0",
      "template": {
        "outputs": [
            {
                "simpleText": {
                    "text": "오늘의 국내증시를 알려드리겠습니다."
                }
            },
          {
            "listCard": {
              "header": {
                "title": "현재 국내증시 입니다."
              },
              "items": [
                {
                  "title": name_1,
                  "description": " 현재가 : " +prices_1+ " / 등락폭 : " + updown_pm_1+" "+updown_1,
                  "link": {
                    "web": "https://finance.naver.com/sise/sise_index.naver?code=KOSPI"
                  }
                },
                {
                  "title": name_2,
                  "description": " 현재가 : " +prices_2+ " / 등락폭 : " + updown_pm_2+" "+updown_2,
                  "link": {
                    "web": "https://finance.naver.com/sise/sise_index.naver?code=KOSDAQ"
                  }
                },
                {
                  "title": name_3,
                  "description": " 현재가 : " +prices_3+ " / 등락폭 : " + updown_pm_3+" "+updown_3,
                  "link": {
                    "web": "https://finance.naver.com/sise/sise_index.naver?code=KPI200"
                  }
                },
                ],
              "buttons": [
                {
                  "label": "자세히 보기",
                  "action": "webLink",
                  "webLinkUrl": "https://m.stock.naver.com/domestic/capitalization/KOSPI"
                }
              ]
            }
          },
            {
                 "simpleText": {
                   "text": "⚠️ 제공되는 정보는 오류 및 지연이 발생될 수 있으므로 유의하시기 바랍니다."
             }
         }
        ],
    "quickReplies": [
        {
        "messageText": "처음으로",
        "action": "message",
        "label": "처음으로"
      },
      {
        "messageText": "해외증시",
        "action": "message",
        "label": "해외증시"
      },
      {
        "messageText": "인기종목",
        "action": "message",
        "label": "인기종목"
      },
      {
        "messageText": "환율",
        "action": "message",
        "label": "환율"
      },
        {
        "messageText": "뉴스",
        "action": "message",
        "label": "뉴스"
         },
        {
         "messageText": "현재가",
         "action": "message",
         "label": "현재가"
        }
        ]

      }
    }
    return jsonify(dataSend)

    
    
    
@application.route('/financeInform', methods = ['POST'])
def financeInform():
    
    html_req = requests.get(url, headers = headers)

    tree = html.fromstring(html_req.text)
    body = tree.xpath('//div[@class ="aside_area aside_popular"]/table[@class="tbl_home"]/tbody')[0]
    company = body.xpath('.//tr/th/a/text()')
    price = body.xpath('.//tr/td[1]/text()')
    updown = body.xpath('tr/@class')
    ratio = body.xpath('.//tr/td[2]/span/text()')
    
    type_url_all = []
    type_urls = body.xpath('./tr/th/a/@href')
    for type_url in type_urls[:5]:
        type_url= 'https://finance.naver.com'+type_url
        type_url_all.append(type_url)
        
    
    company_1 = company[0]
    price_1 = price[0]
    updown_1 = updown[0]
    if updown_1== "up":
         updown_1 = "🔺"
    elif updown_1=="down":
         updown_1="▼"
    else :
          updown_1="-"
            
    ratio_1 = ratio[0]
    type_url_1 = type_url_all[0]
        
    company_2 = company[1]
    price_2 = price[1]
    updown_2 = updown[1]
    if updown_2== "up":
         updown_2 = "🔺"
    elif updown_2=="down":
         updown_2="▼"
    else :
          updown_2="-"
            
    ratio_2 = ratio[1]
    type_url_2 = type_url_all[1]
    
    company_3 = company[2]
    price_3 = price[2]
    updown_3 = updown[2]
    if updown_3== "up":
         updown_3 = "🔺"
    elif updown_3=="down":
         updown_3="▼"
    else :
          updown_3="-"
            
    ratio_3 = ratio[2]
    type_url_3 = type_url_all[2]

    company_4 = company[3]
    price_4 = price[3]
    updown_4 = updown[3]
    if updown_4== "up":
         updown_4 = "🔺"
    elif updown_4=="down":
         updown_4="▼"
    else :
          updown_4="-"
            
    ratio_4 = ratio[3]
    type_url_4 = type_url_all[3]
    
    company_5 = company[4]
    price_5 = price[4]
    updown_5 = updown[4] 
    if updown_5== "up":
         updown_5 = "🔺"
    elif updown_5=="down":
         updown_5="▼"
    else :
          updown_5="-"
            
    ratio_5 = ratio[4]
    type_url_5 = type_url_all[4]
    
    
    dataSend = {
      "version": "2.0",
      "template": {
        "outputs": [
            {
                "simpleText": {
                    "text": "오늘의 인기종목을 알려드리겠습니다."
                }
            },
            {
                "listCard": {
                    "header": {
                        "title": "현재 인기종목 입니다."
                    },
                    "items": [
                {
                  "title": company_1,
                  "description": "현재가 : "+price_1+" / 등락폭 : "+updown_1+" "+ratio_1,
                  "link": {
                     "web": type_url_1
                  }
                },
                {
                  "title": company_2,
                  "description": "현재가 : "+price_2+" / 등락폭 : "+updown_2+" "+ratio_2,
                  "link": {
                     "web": type_url_2
                  }
                },
                {
                  "title": company_3,
                  "description": "현재가 : "+price_3+" / 등락폭 : "+updown_3+" "+ratio_3,
                  "link": {
                     "web": type_url_3
                  }
                },
                {
                  "title": company_4,
                  "description": "현재가 : "+price_4+" / 등락폭 : "+updown_4+" "+ratio_4,
                  "link": {
                     "web": type_url_4
                  }
                },
                {
                  "title": company_5,
                  "description": "현재가 : "+price_5+" / 등락폭 : "+updown_5+" "+ratio_5,
                  "link": {
                     "web": type_url_5
                  }
                }
              ],
              "buttons": [
                {
                  "label": "자세히 보기",
                  "action": "webLink",
                  "webLinkUrl": "https://finance.naver.com/"
                }
              ]
            }
          },
            {
                 "simpleText": {
                   "text": "⚠️ 제공되는 정보는 오류 및 지연이 발생될 수 있으므로 유의하시기 바랍니다."
             }
         }
        ],
    "quickReplies": [
        {
        "messageText": "처음으로",
        "action": "message",
        "label": "처음으로"
      },
      {
        "messageText": "해외증시",
        "action": "message",
        "label": "해외증시"
      },
      {
        "messageText": "국내증시",
        "action": "message",
        "label": "국내증시"
      },
      {
        "messageText": "환율",
        "action": "message",
        "label": "환율"
      },
        {
        "messageText": "뉴스",
        "action": "message",
        "label": "뉴스"
        },
        {
         "messageText": "현재가",
         "action": "message",
         "label": "현재가"
        }
        ]

      }
    }
    return jsonify(dataSend)



@application.route('/nowprice', methods=['POST'])
def nowprice():
    content = request.get_json()
    sys_stockname = content["action"]["params"]["sys_stockname"]
    
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}
    url_1 = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query="+sys_stockname
    html_req = requests.get(url_1, headers=headers)
    tree = html.fromstring(html_req.text)

    name = tree.xpath('//*[@id="_cs_root"]/div[1]/div/h3/a/span[1]/text()')[0]
    price = tree.xpath('//*[@id="_cs_root"]/div[1]/div/h3/a/span[2]/strong/text()')[0]
    updown_pm = tree.xpath('//*[@id="_cs_root"]/div[1]/div/h3/a/span[2]/span[2]/span[2]/text()')[0]
    updown = tree.xpath('//*[@id="_cs_root"]/div[1]/div/h3/a/span[2]/span[2]/em[1]/text()')[0]

    number = tree.xpath('//*[@id="_cs_root"]/div[1]/div/h3/a/em/text()')[0]
    url_2 = "https://finance.naver.com/item/main.naver?code="+number
    
    if updown_pm == "상승":
         updown_pm = "🔺"
    elif updown_pm=="하락":
         updown_pm="▼"
    else :
          updown_pm="-"

    dataSend = {
      "version": "2.0",
      "template": {
        "outputs": [
            {
                "simpleText": {
                    "text": name+" 현재가를 알려드리겠습니다."
                }
            },
          {
            "listCard": {
              "header": {
                "title": "주식 현재가 입니다."
              },
              "items": [
                {
                  "title": name,
                  "description": "종목명",
                  "link": {
                    "web": url_2
                  }
                },
                {
                  "title": price+" "+updown_pm+""+updown,
                  "description": "현재가 / 등락폭 "
                }
              ],
              "buttons": [
                {
                  "label": "자세히 보기",
                  "action": "webLink",
                  "webLinkUrl": "https://finance.naver.com/"
                }
              ]
            }
          },
            {
                 "simpleText": {
                   "text": "⚠️ 장 중에는 조회 시점의 시세이며, 장 이외 시간에는 직전 장 종료 시점의 시세입니다."
                     +"\n"+"⚠️ 제공되는 정보는 오류 및 지연이 발생될 수 있으므로 유의하시기 바랍니다."
             }
         },
        ],
    "quickReplies": [
        {
        "messageText": "처음으로",
        "action": "message",
        "label": "처음으로"
      },
      {
        "messageText": "국내증시",
        "action": "message",
        "label": "국내증시"
      },
      {
        "messageText": "해외증시",
        "action": "message",
        "label": "해외증시"
      },
      {
        "messageText": "인기종목",
        "action": "message",
        "label": "인기종목"
      },
      {
        "messageText": "환율",
        "action": "message",
        "label": "환율"
      },
        {
        "messageText": "뉴스",
        "action": "message",
        "label": "뉴스"
        },
        {
         "messageText": "현재가",
         "action": "message",
         "label": "현재가"
        }
        ]

      }
    }
    return jsonify(dataSend)

    
    
if __name__ == "__main__":
    application.run(host='0.0.0.0', port=int(sys.argv[1]), debug=True)
    
    