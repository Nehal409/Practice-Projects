require('dotenv').config();  
const AWS = require('aws-sdk');
const fs = require('fs');
const path = require('path');

const bucketName = process.env.BUCKET_NAME; 
// links the root path of the project with the folder that holds the audio files.
const localDirectories = [
  'dr-israr-ahmed',
  'dr-zakir-nayak',
  'junaid-jamshed',
  'molana-Ibadullah',
];

const localPaths = localDirectories.map((directory) => {
  return path.join(__dirname, directory);
});

// setting AWS s3 credentials
const s3 = new AWS.S3({
  accessKeyId: process.env.ACCESS_KEY_ID,
  secretAccessKey: process.env.SECRET_ACCESS_KEY
});

// Function to upload a file to S3
function uploadFileToS3(filePath,folderName) {
  // Read contents of the file
  const fileStream = fs.createReadStream(filePath);
  fileStream.on('error', function (err) {
    console.log('File Error', err);
  });

  // Define the S3 object parameters for the file to be uploaded
  const s3Params = {
    Bucket: bucketName,
    Key: `${folderName}/${path.basename(filePath)}`,
    Body: fileStream,
  };

  // Upload the file to S3 using the specified S3 object parameters.
  s3.upload(s3Params, function (err, data) {
    if (err) {
      console.log('Error uploading file:', err);
    } else {
      console.log('File uploaded successfully:', data.Location);
    }
  });
}

// Function to get all audio files in the local directory
function getAudioFilesInDirectory(directory) {
  // Read the contents of the specified directory synchronously and store the results in an array.
  const files = fs.readdirSync(directory);
  // Filter the files array to only include audio files (MP3, WAV, and FLAC).
  const audioFiles = files.filter((file) => {
    const ext = path.extname(file);
    return ['.mp3', '.wav', '.flac'].includes(ext);
  });
  return audioFiles;
}

// Loop through each local directory and upload each audio file to the corresponding folder in S3
localPaths.forEach((localDirectory, i) => {
// Get all audio files in the local directory and upload each one to S3
const audioFiles = getAudioFilesInDirectory(localDirectory);
console.log(`Uploading ${audioFiles.length} audio files to S3...`);
// Iterate through each audio file and upload it to the S3 bucket.
audioFiles.forEach((file) => {
  // Creates the full path to the current audio file in the local directory 
  const filePath = path.join(localDirectory, file);
  const folderName = localDirectories[i];
  uploadFileToS3(filePath,folderName);
});
})
