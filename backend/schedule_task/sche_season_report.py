# =========================== #
# -*- coding: utf-8 -*-       #
# @Time : 22/2/7 16:32     #
# @Author : 毕磊              #
# @Site : ---                 #
# @File : sche_season_report.mypy          #
# @Software: PyCharm  #
#
# =========================== #
import log
import mypy.akshare_data.as_em_yjbb_kb as bb_kb
import mypy.tools.financial_report_tool as frt
import mypy.akshare_data.as_em_zcfz as zcfz
import mypy.tools.financial_report_tool as frt
import mypy.choice.choice_strategy as choices

#更新东财季报
def get_allreport(global_data):
    if frt.is_fina_report_time() == False:
        log.info("不是发布快报的时段,pass")
        return
    get_em_seasonreport()

#更新东财财务快报,这会变更财务报表更新的逻辑
def get_em_seasonreport():
    #获取东财的季报和快报,并同步给内部季报表,并更新PE估值表
    fetcher = bb_kb.Fetcher()
    fetcher.allProcess()
    log.info("东财的原始季报和快报抓取并同步计算my季报表完毕")
    #获取资产负债表,并同步给内部季报表
    f2 = zcfz.Fetcher(frt.get_emkb_season_code())
    f2.allProcess()
    log.info("东财的资产负债表抓取完毕,并同步my季报表和PE表完毕")
    choices.run_dealer('季报策略')



if __name__ == '__main__':
    print(frt.get_emkb_season_code('20220401'))
