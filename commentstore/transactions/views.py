from django.db import transaction
from django.shortcuts import render
from django.contrib import messages
from . import models
from transactions.forms import PointsTransferForm


def points_view(request):
    all_points = models.Points.objects.all()
    return render(request, "transactions/points.html", {"all_points": all_points})


def points_transfer(request):
    if request.method == 'POST':
        form = PointsTransferForm(request.POST)

        if form.is_valid():
            src_username = form.cleaned_data["enter_your_username"]
            dst_username = form.cleaned_data["enter_destination_username"]
            points_to_transfer = form.cleaned_data["enter_points_to_transfer"]

            try:
                src_points = models.Points.objects.get(name__username=src_username)
                dst_points = models.Points.objects.get(name__username=dst_username)

                if src_points.points < points_to_transfer:
                    messages.error(request, "转账失败：积分余额不足")
                    return render(request, "transactions/pointstransfer.html", {"form": form})

                with transaction.atomic():
                    src_points.points = src_points.points - points_to_transfer
                    src_points.save()

                    dst_points.points = dst_points.points + points_to_transfer
                    dst_points.save()

                all_points = models.Points.objects.all()
                messages.success(request, "转账成功！")
                return render(request, "transactions/points.html", {
                    "src_points": src_points,
                    "dst_points": dst_points,
                    "all_points": all_points
                })

            except models.Points.DoesNotExist:
                messages.error(request, "转账失败：用户名不存在")
                return render(request, "transactions/pointstransfer.html", {"form": form})

        return render(request, "transactions/pointstransfer.html", {"form": form})

    else:
        form = PointsTransferForm()

    return render(request, "transactions/pointstransfer.html", {"form": form})
