# -*- coding: utf-8 -*-
import scrapy
import json
from haiwai.items import HaiwaiItem

class UsernameSpider(scrapy.Spider):
    name = 'username'
    allowed_domains = ['stocktwits.com']
    usstocks = ["APHB","THM","AWX","MTNB","WRN","NAVB","SPSB","AMZA","IYM","MOO","NHS","SPHB","FDM","CIK","FHLC","BSCL","WFC-W","AGGY","SPEM","IWS","IHI","FVD","BIL","DON","JXI","EVM","FNGD","DRN","SLYV","EMLP","TECL","VTEB","SPHQ","VOOG","THD","VOX","IBDK","XAR","VUSE","TCF-D","IWV","CORN","ASHS","FBT","FXU","TDTT","FQAL","FNDX","VOE","GEM","VCR","FDMO","SCHK","LRGF","IQDF","CORP","VOT","FNDF","SLYG","SCJ","JPM-A","PSI","VBR","IYH","MGY+","WFC-Y","PLTM","HSPX","FXA","VNLA","SPAB","GNR","PRE-H","SSW-D","ERC","DEUS","TLTD","JPUS","PJP","VXF","CLNY-G","VIS","NLY-G","FFEU","CVY","SPTS","AIEQ","BLV","TOO-A","HUSV","FXY","EEB","XMLV","DBB","EEV","GXC","MXI","IXN","SLX","DTD","DPST","SMDD","DTN","IXG","MDYV","IHY","WFC-Q","VKI","GLU","AHT-D","CHIX","STT-D","SJB","IBDP","SPFF","EXT","GSG","FPEI","FEU","BRF","TIPX","STIP","SUB","AOM","RWO","BBT-F","SHM","FXH","NFRA","MLPX","SGDM","WIP","HNW","IPE","BDCL","USFR","GS-J","FLGE","IJJ","USL","JPIN","TDTF","XLG","PALL","CANE","XHE","MDYG","BSJQ","JHSC","SPYX","MVV","QAI","FDIS","BIZD","AEF","BSCO","SHYD","SPMD","HDGE","FNDB","UCON","TOTL","EIS","UCI","BSJK","BSCP","BAB","RYF","EPV","IDEV","RYH","FIDU","GAMR","MBG","EES","ATMP","IBDR","RLY","PSP","PUTW","IEZ","JHML","IXP","FIW","DWM","IBND","FBND","IVLU","DBEM","SDPI","TRX","LTS","CANF","UAMY","UGAZ","EWZ","UVXY","TNA","IBDQ","DIA","RSX","JNUG","EWX","VOO","BZQ","DWT","SPXL","SPY","IWM","UBOT","IBDL","SVXY","FXI","TWM","RDIV","PHYS","IVV","DUST","YANG","GDXJ","GLD","UWT","EEM","TMV","BRZU","CQQQ","INDA","XOP","DGAZ","OILU","CWB","OILD","MTUM","IBDS","CVM","NOBL","UNG","HYIH","IEFA","NUMG","PLCY","CSM","IETC","SMDV","ICOW","FFHG","JPGB","CNYA","OIH","IDHD","XUSA","PBTP","BBAX","XSHD","ENOR","FIBR","IZRL","VAMO","ACES","TTAI","VT","ICF","STOT","EEMV","IYLD","RGLB","ZBZX","HYDB","EURZ","FLQM","EFNL","VFLQ","SHAG","ITB","GAA","NUMV","SMMV","MAGA","TAIL","IEDI","EZU","DEFA","EFAV","IPFF","PRNT","IAGG","SCHE","FYLD","ARCM","VEA","QMOM","USMV","ACSI","CEFS","QDIV","KNG","DYLS","LQD","PTLC","ACWV","ESML","EWUS","EVIX","NUEM","PEX","GCOW","VXZB","LVUS","BBJP","EMTL","IYJ","GDVD","OILK","DVEM","CALF","PJUL","EMLC","IMOM","PICK","GHYG","DTEC","FTVA","SFHY","QXGG","DDLS","FFTG","JPHY","QXTR","DYB","IBMM","FLQL","VLUE","ICVT","SECT","IEIH","EXIV","USMF","ASHR","ECH","DEWJ","EMGF","FLDR","VFVA","EYLD","PAVE","DRIP","BBEU","BEMO","ALFA","BOSS","IEFN","IECS","LVHI","GSEW","EMHY","HEEM","SLVP","IGHG","NURE","LVHE","IBML","RPUT","IEC","AAU","NG","PFNX","SENS","DXR","PWS","IYZ","IDV","REEM","IEME","UJUL","LEAD","NULG","IEHS","WFIG","NANR","VFMF","GOVT","SJNK","COWZ","USHY","EDEN","FLOT","DIVB","TMFC","LVHB","HYHG","FFTI","DHDG","USO","DDWM","OYLD","PTNQ","ICSH","IGVT","IVAL","BBCA","RVRS","PTMC","REFA","DRSK","VFMO","EFAD","SMMD","VFQY","PSMM","TTAC","EWGS","NEAR","GARD","OQAL","FFSG","SOVB","TCTL","ALTS","DFND","EMSH","IJH","NULV","QVAL","PTEU","PFFD","QUAL","ITOT","SMIN","IGE","NUGT","EMIH","MSUS","IQDG","IXJ","EFV","REGL","GUDB","HYXU","MRGR","IAUF","EMDV","ITA","MEAR","OMFL","LQDI","IGV","NUDM","JPST","CEMB","PREF","VFMV","VMOT","WFHY","BJUL","NUSC","IGRO","IEO","EPRF","HEFA","SLT","EFG","EUDV","SH","FCG","REM","AGT","IYT","OVLU","TIP","GVI","IGEB","DBEU","SOXS","EWW","XLP","UPRO","KWEB","SDS","XLU","RWR","SDOW","XLV","AMJ","SKF","ARKW","EWA","FAZ","VTI","BNO","XRT","TZA","IJR","HEDJ","FDL","VDE","VISI","SPTL","FXO","CWI","MUB","KOL","IPAY","PBW","CGW","FDVV","PAK","CHAD","REET","UYG","DLN","MGC","IBDM","IBDN","ROM","IJS","PSA-Z","FPX","FAX","EZM","BSCJ","INTF","FRLG","DFEN","HUSE","DIV","QDF","IPAC","HYLB","FXF","USRT","MS-K","RJI","WFC-T","VRP","AGO-E","NLY-D","BLOK","SIL","NML","ECF","KORU","FENY","EELV","PSA-U","IDLV","BSCK","SPSM","PFXF","SCHC","BAC-C","EURL","AOK","BAR","PWB","DSI","VIOO","IHF","GWX","ARKG","BFOR","FRI","FNDE","USB-H","NBH","KSA","USB-M","GS-A","SBIO","GMOM","FXD","MGK","LEMB","GLDM","SEA","NAIL","IVOO","ZROZ","RFDA","FCOM","BSCN","GBIL","NORW","GM+B","LQDH","C-J","PBS","WPS","EIM","FIHD","FLTR","HLM-","VMM","LTPZ","REMX","MRRL","JPEM","AGZ","BSCM","OUSA","FMAT","JHMD","HYLD","MUNI","SMN","SRS","GSLC","GRNB","FCO","FRN","IHDG","IDOG","PGHY","TPYP","COPX","EDIV","DZZ","HYMB","GLTR","FNDA","GVAL","XNTK","ITE","JPHF","CMF","EUSC","GCC","SCIF","ARKQ","FNDC","XMPT","BSJL","IWC","KNOW","CHIM","RXI","XPP","CEV","RSXJ","SPPP","DOL","VIOG","SRE-A","FLJP","IQLT","CORR-A","CTO","FLCH","TPOR","BBRE","BDC-B","BYLD","BSJP","DRV","MJCO","EMAN","BTN","FRC-I","USEQ","AUSF","IRBO","MIDU","GS-D","SOYB","DTH","AOR","YUMA","BSJN","ENX","ESBA","RYE","XSW","ALL-G","DGL","JPM-H","GGT-E","BSJM","HECO","UGL","CIM-A","CBL-D","SEF","TILT","QEFA","GTO","REZ","PEB-C","GASX","VFL","IHE","BML-G","EQC-D","JPME","ACWF","BSCQ","MLPQ","BVAL","IBMK","SPDN","QUS","UGA","HAWX","DBP","LFEQ","IVOV","DLR-I","FLTB","ZMLP","C-N","IBDC","RETL","RTH","RXL","DBAW","FCOR","ACU","MLSS","ILTB","MS-F","FBGX","HMLP-A","SMB","CAPE","TGP-B","IMTB","COF-H","QQQE","BJK","FRC-G","GAB-G","BWZ","JHMM","CUT","OUSM","GRES","EWV","REW","REED","XRLV","UAVS","DXF","UMH-C","TFLO","ISCF","CIX","PSMC","CPER","SAA","DMF","GII","ROUS","PXLG","VIOV","IGN","BBT-G","MEXX","JKE","ONLN","BSCS","QDEF","QARP","QLTA","DBEZ","GGO","TOO-B","PSMB","PCG-E","FTV-A","FDLO","FIEE","PWZ","BRN","FIDI","IYY","MS-A","COF-C","ETP-C","BK-C","BLES","FINZ","WFC-P","STT-G","RWL","PEK","EWK","FRAK","TYO","USVM","TRTY","ARI-C","SSW-H","COF-P","INSW-A","PSA-X","SPDV","TKAT","SIJ","CCOR","KIM-I","GLL","DZK","APO-A","WRB-B","LGLV","USAI","DIM","ITEQ","TNP-F","GSSC","CJNK","RHE-A","BSJO","BLHY","WBIE","WRB-C","SF-A","PCG-G","EPS","JPNL","HYGV","SHYL","UMDD","LOV","JKL","USOU","JKF","RYAM-A","SCE-J","NEN","EZJ","INN-E","SMLF","WPG-H","FLQE","CDR-C","ACIM","USOD","ROAM","DUSL","RAAX","EUFL","CCI-A","MZZ","TBX","DX-B","DJD","HYLV","SB-C","ISMD","PWC","XKII","VCF","PBJ","JPSE","LMLP","MMIN","CMRE-C","PXSG","FTLS","CDR-B","JKH","TMK-C","SCE-H","ERM","MNI","RWK","JCAP-B","WTMF","FLGB","GAL","DVYL","ELLO","IPO","KCE","SUSA","CSD","KFYP","DD-B","ENFR","AFIF","RYJ","SYV","FDHY","PPTY","VSGX","ESGV","SPUU","ISRA","RWJ","GEX","ZHOK","BTAL","ULST","CIM-C","SSW-I","FVAL","RYU","OLO","ARE-D","IWL","GGZ-A","BBP","JPM-D","DBS","TOLZ","CNXT","SRVR","XAN-C","FSI","TERM","UOCT","POCT","BOCT","SBB","KCCB","IBDT","VEGI","EUMV","FLIY","PPLC","UJPY","HIPS","INDS","WDIV","ECNS","SDYL","DBLV","TYD","JHEM","WDRW","JMST","WMW","PSR","ESPO","IMLP","MFMS","JMUB","EAGG","RTL","PAWZ","IBMN","EASG","OIL","SGG","GLOP-C","COW","CMDY","JO","NEED","WANT","BC-B","FLFR","PASS","SMHB","HMG","PLAG","PRK","HEB","GPL","TALO+","IPOA=","BJAN","CCC+","HEXO","TAWK","RWGV","RWVG","RWSL","AGE","LHC+","JCPB","JPM-C","TPAY","XMX","ARKF","ALEC","GOSS","ZYXI","IMAC","AVDR","TCRR","CTRM","MITO","BEST","SOLY","VFF","VPC","VRAI","IGC","SLGG","FDEM","KLDO","MR","FIVG","SWAV","AL-A","CRSAU","FHL","GDNA","GFIN","GDAT","GBUY","BBSA","PSA-H","BBUS","LSLT","AIG-A","BIOX","DHR-A","TRNE=","NEE-N","TRTN-A","OSW","BPYPP","CIC+","RYZZ","GNFT","CARE","HHHH","DTIL","WTRE","JAMF","PUYI","LYFT","BAPR","UAPR","PAPR","DUK-A","PBTS","RUHN","IBMO","SILK","NGM","OXSQZ","VERB","IBKCN","FISR"]
    uindex = 0
    urls = []
    for symbol in usstocks:
        urls.append('https://api.stocktwits.com/api/2/streams/symbol/'+symbol+'.json?filter=top')
    # baseUrl = 'https://api.stocktwits.com/api/2/streams/symbol/AMZN.json?filter=top'
    start_urls = urls

    def parse(self, response):
        body = json.loads(response.body)
        maxstr = body['cursor']['max']
        symbol = body['symbol']['symbol']
        title = body['symbol']['title']
        watchlist_count = body['symbol']['watchlist_count']
        for message in body['messages']:
            item = HaiwaiItem()
            pinglun = message['body']
            created_at = message['created_at']
            sourcetitle = message['source']['title']
            # symbols = ''
            # for symbol in message['symbols'][0]:
            #     symbols = symbol[''] + ',' 
            username = message['user']['username']
            followers = message['user']['followers']
            following = message['user']['following']
            join_date = message['user']['join_date']
            name = message['user']['name']
            watchlist_stocks_count = message['user']['watchlist_stocks_count']
            item['symbol'] = symbol
            item['title'] = title
            item['watchlist_count'] = watchlist_count
            item['pinglun'] = pinglun
            item['created_at'] = created_at
            item['sourcetitle'] = sourcetitle
            item['username'] = username
            item['followers'] = followers
            item['following'] = following
            item['join_date'] = join_date
            item['name'] = name
            item['watchlist_stocks_count'] = watchlist_stocks_count
            yield item
            print('..........', username, pinglun, sourcetitle, join_date)

        url = response.url + '&max=' + str(maxstr)
        print(',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,', url)
        yield scrapy.Request(url=url, callback = self.parse)


        
