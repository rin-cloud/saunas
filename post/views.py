from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from top.models import SaunaInfo   # モデルのインポート

@csrf_exempt  # 本番環境ではCSRF保護を無効にしないでください
def post_template(request):
    if request.method == 'POST':
        # フォームから送信されたデータを取得
        store_name = request.POST.get('store_name')
        water_bath_rating = request.POST.get('water_bath_rating')
        sauna_rating = request.POST.get('sauna_rating')
        indoor_outdoor_rating = request.POST.get('indoor_outdoor_rating')
        access = request.POST.get('access')
        sauna_impression = request.POST.get('sauna_impression')
        image_upload = request.FILES.get('image_upload')  # ファイルは request.FILES から取得

        # SaunaInfo オブジェクトを作成してデータベースに保存
        sauna_info = SaunaInfo(
            store_name=store_name,
            cold_bath_rating=water_bath_rating,
            sauna_rating=sauna_rating,
            indoor_outdoor_rating=indoor_outdoor_rating,
            access=access,
            sauna_review=sauna_impression,
            store_image=image_upload  # ファイルオブジェクトを直接割り当てる
        )
        sauna_info.save()

        return redirect('top_template')  # 'top_template' はトップページのビュー名です

    # GETリクエストの場合、またはフォームのデータが必要でない場合
    # 初期フォームページを表示
    return render(request, 'post.html') 