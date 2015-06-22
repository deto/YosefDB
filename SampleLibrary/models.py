import uuid;
from django.db import models
from django.contrib.auth.models import User;

# Create your models here.

class Upload(models.Model):
    UploadedBy = models.ForeignKey(User, null=True, on_delete=models.SET_NULL);
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

class UnvalidatedUpload(models.Model):
    UploadedBy = models.ForeignKey(User, null=True, on_delete=models.SET_NULL);
    UploadDate = models.DateTimeField(auto_now_add=True);
    UploadId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False);
    UnrecognizedCols = models.CharField(max_length=2000);

    def __unicode__(self):
        return self.UploadedBy + ": " + str(self.UploadDate);

    def create_valid_upload(self):
        """
        Similar to UnvalidatedSample.create_valid_sample
        Creates a valid Upload object from the unvalidated object
        :return: an Upload object
        """
        upload = Upload();
        upload.UploadedBy = self.UploadedBy;
        return upload; #Date is added automatically, no unrecognized cols

class UnvalidatedSample(models.Model):
    SampleId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False);
    UploadBatch = models.ForeignKey(UnvalidatedUpload);
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

    def create_valid_sample(self):
        sample = Sample();
        sample.Organism = self.Organism;
        sample.Tissue = self.Tissue;
        sample.ExperimentName = self.ExperimentName;
        sample.DataType = self.DataType;
        sample.GenomeVersion = self.GenomeVersion;
        sample.ExperimentDescription = self.ExperimentDescription;
        sample.isSingleCell = self.isSingleCell;
        sample.isPublishedData = self.isPublishedData;
        sample.Date = self.Date;
        sample.Batch = self.Batch;
        sample.SequencingTech = self.SequencingTech;
        sample.RawFileLoc = self.RawFileLoc;
        sample.SpecificRawFileLoc = self.SpecificRawFileLoc;
        sample.LocalBackupLoc = self.LocalBackupLoc;
        sample.RemoteBackupLoc = self.RemoteBackupLoc;
        sample.ProcessedFileLoc = self.ProcessedFileLoc;
        sample.ConditionCode = self.ConditionCode;
        sample.TimeCode = self.TimeCode;
        sample.BatchCode = self.BatchCode;
        sample.IdCode = self.IdCode;
        sample.ControlId = self.ControlId;
        sample.PreprocessDate = self.PreprocessDate;
        sample.Comments = self.Comments;

        return sample;



