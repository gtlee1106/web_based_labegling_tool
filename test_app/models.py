from django.db import models
import datetime


# Create your models here.
class DataSet(models.Model):
    dataset_name = models.CharField(max_length=1024)
    # data set owner may be necessary but now, skip!
    dataset_desc = models.TextField()  # 추가로 옵션이 더 필요하려나?
    # input type. enum 같은 타입이 있으면 좋겠군. 이미지 / 텍스트 등
    dataset_input_type = models.CharField(max_length=64)
    # output type. classification / regression / image for seg, etc
    dataset_output_type = models.CharField(max_length=64)
    is_private = models.BooleanField(default=False)
    create_datetime = models.DateTimeField(default=datetime.datetime.now())
    modify_datetime = models.DateTimeField(default=datetime.datetime.now())
    is_deleted = models.BooleanField(default=False)


class DataSetItem(models.Model):
    dataset = models.ForeignKey(DataSet, on_delete=models.CASCADE)
    data_type = models.CharField(max_length=64)  # dataset에서 표현을 해주긴 할 텐데 음...
    # 가능한 데이터 형태
    # 1. 벡터(1차원 포함)
    # 2. 이미지
    # 3. 텍스트
    # 4. 기타 등등
    data = models.TextField()  # 이걸로 넣고, 보여줄 때는 파싱해서 보여줄 수 있지 않을까...?


class DataSetItemLabel(models.Model):
    datasetitem = models.ForeignKey(DataSetItem, on_delete=models.CASCADE)  # 음... 1개 데이터에 대해서 여러명이 라벨을 붙일 수도 있어서...?
    label = models.TextField()  # 가능한 라벨...? classification 같은 경우, 라벨 1개에 대해서 여러개 데이터가 붙을 수 있군 -_-;
    # or 여러개 두고 내가 직접 처리하게 할까...
    labeler = models.CharField(max_length=64)  # 레이블러 이름을 일단은 char field로 써두자.
    labeled_datetime = models.DateTimeField(default=datetime.datetime.now())
