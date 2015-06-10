import uuid;
from django.db import models

# Create your models here.

class Upload(models.Model):
    UploadedBy = models.CharField(max_length=100);
    UploadDate = models.DateTimeField(auto_now_add=True);
    UploadId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False);

    def __unicode__(self):
        return self.UploadedBy + ": " + str(self.UploadDate);

class Sample(models.Model):
    SampleId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False);
    UploadBatch = models.ForeignKey(Upload);
    Organism = models.CharField(max_length=200);
    Tissue = models.CharField(max_length=200);
    ExperimentName = models.CharField(max_length=200);
    DataType = models.CharField(max_length=50);
    GenomeVersion = models.CharField(max_length=100);
    ExperimentDescription = models.CharField(max_length=500);
    isSingleCell = models.BooleanField(default=False);
    isPublishedData = models.BooleanField(default=False);
    Date = models.DateField(null=True);
    Batch = models.CharField(max_length = 50);
    SequencingTech = models.CharField(max_length=200);
    RawFileLoc = models.CharField(max_length=200);
    SpecificRawFileLoc = models.CharField(max_length=200);
    LocalBackupLoc = models.CharField(max_length=200);
    RemoteBackupLoc = models.CharField(max_length=200);
    ProcessedFileLoc = models.CharField(max_length=200);
    ConditionCode = models.IntegerField(null=True);
    TimeCode = models.IntegerField(null=True);
    BatchCode = models.IntegerField(null=True);
    IdCode = models.IntegerField(null=True);
    ControlId = models.IntegerField(null=True);
    PreprocessDate = models.DateField(null=True);
    Comments = models.CharField(max_length=200);

    #Need this so admin tools display it correctly
    def __unicode__(self):
        return self.ExperimentName + ": " + str(self.IdCode);


