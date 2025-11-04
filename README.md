# Image Processing n8n Workflow

This repository contains a comprehensive n8n workflow for processing images with AI-powered analysis, OCR, and transformations.

## Features

The workflow includes the following capabilities:

### 🎯 Core Features
- **Webhook Trigger**: Upload images via HTTP POST request
- **AI Vision Analysis**: Analyzes images using OpenAI's Vision API to describe content, objects, colors, and context
- **OCR Text Extraction**: Extracts any text found in the image
- **Image Resizing**: Automatically resizes images to optimal dimensions
- **Metadata Extraction**: Extracts EXIF and other metadata from images
- **Multiple Output Options**: Save to disk, upload to S3, or return JSON response

### 📋 Workflow Steps

1. **Webhook - Upload Image**: Receives the image via POST request
2. **Extract Image Data**: Processes the incoming data and prepares the image
3. **Parallel Processing**:
   - AI Vision Analysis (OpenAI Vision API)
   - OCR Text Extraction
   - Image Resizing (800x600, max area)
   - Metadata Extraction
4. **Merge Results**: Combines all analysis results
5. **Format Output**: Creates a structured JSON response
6. **Send Response**: Returns the complete analysis to the caller
7. **Optional Storage**: Save to disk or upload to S3

## Setup Instructions

### 1. Import the Workflow

1. Open your n8n instance
2. Go to **Workflows** → **Import from File**
3. Select `image-processing-workflow.json`
4. The workflow will be imported and ready to configure

### 2. Configure Credentials

#### OpenAI API (Required for AI Analysis)
1. Go to **Credentials** in n8n
2. Add new credential → **OpenAI API**
3. Enter your OpenAI API key
4. Name it "OpenAI API"

#### AWS S3 (Optional - for cloud storage)
1. Go to **Credentials** in n8n
2. Add new credential → **AWS**
3. Enter your AWS Access Key ID and Secret Access Key
4. Name it "AWS Credentials"
5. Set environment variable `S3_BUCKET` with your bucket name

### 3. Activate the Workflow

1. Click the toggle in the top-right to activate the workflow
2. The webhook URL will be generated (e.g., `https://your-n8n-instance.com/webhook/upload-image`)

## Usage

### Upload an Image via cURL

```bash
curl -X POST https://your-n8n-instance.com/webhook/upload-image \
  -F "image=@/path/to/your/image.jpg"
```

### Upload with Python

```python
import requests

url = "https://your-n8n-instance.com/webhook/upload-image"
files = {'image': open('photo.jpg', 'rb')}
response = requests.post(url, files=files)
print(response.json())
```

### Upload with JavaScript/Node.js

```javascript
const FormData = require('form-data');
const fs = require('fs');
const axios = require('axios');

const form = new FormData();
form.append('image', fs.createReadStream('photo.jpg'));

axios.post('https://your-n8n-instance.com/webhook/upload-image', form, {
  headers: form.getHeaders()
})
.then(response => console.log(response.data))
.catch(error => console.error(error));
```

### Upload with Postman

1. Create a new POST request
2. URL: `https://your-n8n-instance.com/webhook/upload-image`
3. Body → form-data
4. Add key "image" of type "File"
5. Select your image file
6. Send the request

## Response Format

The workflow returns a JSON response with the following structure:

```json
{
  "originalImage": {
    "fileName": "photo.jpg",
    "mimeType": "image/jpeg",
    "fileSize": 245678,
    "uploadedAt": "2025-11-04T12:00:00.000Z"
  },
  "aiAnalysis": {
    "description": "This image shows a sunset over a beach with palm trees...",
    "model": "gpt-4-vision-preview"
  },
  "ocrText": "Any text extracted from the image appears here",
  "metadata": {
    "width": 1920,
    "height": 1080,
    "format": "jpeg",
    "exif": { ... }
  },
  "processedAt": "2025-11-04T12:00:01.000Z"
}
```

## Customization Options

### Modify Image Resize Dimensions
Edit the "Resize Image" node:
- `newWidth`: Change from 800 to your desired width
- `newHeight`: Change from 600 to your desired height
- `quality`: Adjust JPEG quality (0-100)

### Customize AI Analysis Prompt
Edit the "AI Vision Analysis" node prompt to focus on specific aspects:
```javascript
"Analyze this image and identify all products visible"
"Describe the architectural style and building features"
"List all people in the image and their activities"
```

### Enable Storage Options
1. **Save to Disk**: Enable the "Save Original to Disk" node and configure the path
2. **Upload to S3**: Enable the "Upload to S3" node, add AWS credentials, and set the bucket name

### Add More Processing Steps
You can extend the workflow with:
- Image filtering and effects
- Object detection
- Face recognition
- Color palette extraction
- Image comparison
- Watermarking
- Format conversion

## Troubleshooting

### Common Issues

**Issue**: "OpenAI credentials not found"
- **Solution**: Make sure you've added OpenAI API credentials and they're named exactly "OpenAI API"

**Issue**: "Binary data not found"
- **Solution**: Ensure you're uploading the image as form-data with the key "image"

**Issue**: OCR not working
- **Solution**: Some image formats may not be supported. Try converting to JPEG or PNG first

**Issue**: Timeout errors
- **Solution**: Large images may take time to process. Increase the webhook timeout in workflow settings

## Requirements

- n8n instance (self-hosted or cloud)
- OpenAI API key (for AI vision analysis)
- AWS account (optional, for S3 storage)

## License

MIT License - Feel free to modify and use as needed!

## Support

For issues or questions:
1. Check n8n documentation: https://docs.n8n.io
2. n8n community forum: https://community.n8n.io
3. OpenAI API docs: https://platform.openai.com/docs

---

**Note**: This workflow uses the OpenAI Vision API which incurs costs based on usage. Monitor your API usage to avoid unexpected charges.
