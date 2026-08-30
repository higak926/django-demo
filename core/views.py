from django.http import JsonResponse
from .models import Memo


def memo_list_api(request):
    # データベースからメモの一覧を取得し、辞書のリストに変換
    memos = list(
        Memo.objects.values('id', 'title', 'content', 'created_at').order_by(
            '-created_at'
        )
    )
    return JsonResponse({'memos': memos})
