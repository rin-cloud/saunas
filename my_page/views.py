from django.shortcuts import render
 # 以下のパスはあなたのプロジェクトの構造に応じて変更してください。
from top.models import SaunaInfo  # 'top'はDjangoアプリケーション名、'SaunaInfo'はモデルクラス名

def my_page_template(request):
    # 'top_saunainfo' テーブルから全てのレコードを取得
    saunas = SaunaInfo.objects.all()

    # テンプレートに渡すためのリストを作成
    shopList = []
    for sauna in saunas:
        shopList.append({
            'name': sauna.store_name,
            'access': sauna.access,
            # 評価は必要に応じて平均を取るなどして計算
            'evaluation': str((sauna.cold_bath_rating + sauna.sauna_rating + sauna.indoor_outdoor_rating) / 3)
        })

    # テンプレートに渡すコンテキストデータ
    context = {
        "shop": shopList
    }
    return render(request, 'my_page.html', context)