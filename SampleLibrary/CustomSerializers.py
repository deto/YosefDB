import json;

def sample_to_dict(sample):
    temp = dict();
    temp["SampleId"] = str(sample.SampleId);
    temp["UploadBatch"] = str(sample.UploadBatch_id);
    temp["UploadDate"] = str(sample.UploadBatch.UploadDate);
    uploader = sample.UploadBatch.UploadedBy;
    temp["Uploader"] = uploader.first_name + " " + uploader.last_name;
    temp["Organism"] = sample.Organism;
    temp["Tissue"] = sample.Tissue;
    temp["ExperimentName"] = sample.ExperimentName;
    temp["DataType"] = sample.DataType;
    temp["GenomeVersion"] = sample.GenomeVersion;
    temp["ExperimentDescription"] = sample.ExperimentDescription;
    temp["isSingleCell"] = sample.isSingleCell;
    temp["isPublishedData"] = sample.isPublishedData;
    temp["Date"] = str(sample.Date);
    temp["Batch"] = sample.Batch;
    temp["SequencingTech"] = sample.SequencingTech;
    temp["RawFileLoc"] = sample.RawFileLoc;
    temp["SpecificRawFileLoc"] = sample.SpecificRawFileLoc;
    temp["LocalBackupLoc"] = sample.LocalBackupLoc;
    temp["RemoteBackupLoc"] = sample.RemoteBackupLoc;
    temp["ProcessedFileLoc"] = sample.ProcessedFileLoc;
    temp["ConditionCode"] = sample.ConditionCode;
    temp["TimeCode"] = sample.TimeCode;
    temp["BatchCode"] = sample.BatchCode;
    temp["IdCode"] = sample.IdCode;
    temp["ControlId"] = sample.ControlId;
    temp["PreprocessDate"] = str(sample.PreprocessDate);
    temp["Comments"] = sample.Comments;
    return temp;

def upload_to_dict(upload):
    temp = dict();
    temp["UploadId"] = str(upload.UploadId);
    temp["UploadDate"] = str(upload.UploadDate);
    temp["UploadedBy"] = upload.UploadedBy.first_name + " " + upload.UploadedBy.last_name;
    return temp;


def serialize_sample(sample):
    sdict = sample_to_dict(sample);
    return json.dumps(sdict);

def serialize_samples(sample_list):
    all_samples = [sample_to_dict(sample) for sample in sample_list];
    return json.dumps(all_samples);

def serialize_upload(upload):
    udict = upload_to_dict(upload);
    return json.dumps(udict);

def serialize_uploads(upload_list):
    all_uploads = [upload_to_dict(upload) for upload in upload_list];
    return json.dumps(all_uploads);

