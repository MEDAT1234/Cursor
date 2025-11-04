# n8n AI Video Creation Workflow

This workflow creates videos from AI-generated images based on the screenshot provided.

## Workflow: "SHIFT 1 - Create Video Using AI Image"

### Overview
This workflow automates the process of:
1. Generating an AI image from a text prompt
2. Converting that image into a video using AI
3. Polling for video completion
4. Downloading and saving the final video

### Workflow Steps

1. **Manual Trigger** - Start the workflow manually
2. **Generate AI Image** - Uses OpenAI API to create an image from a text prompt
3. **Download Image** - Downloads the generated image
4. **Image to Video AI** - Converts the image to video using Stability AI
5. **Check Video Status** - Polls the API to check if video generation is complete
6. **Is Complete?** - Conditional check for video completion status
7. **Wait** - If not complete, waits 10 seconds before checking again (creates a loop)
8. **Download Video** - Once complete, downloads the generated video
9. **Save to File** - Saves the video to the local filesystem

### How to Import

1. Open your n8n instance
2. Click on "Workflows" in the left sidebar
3. Click "Import from File" or "Import from URL"
4. Select the `n8n-create-video-workflow.json` file
5. The workflow will be imported and ready to configure

### Required Credentials

Before running this workflow, you'll need to set up:

1. **OpenAI API** credentials
   - Sign up at https://platform.openai.com/
   - Generate an API key
   - Add credentials in n8n under "Credentials" → "OpenAI"

2. **Stability AI API** credentials
   - Sign up at https://stability.ai/
   - Generate an API key
   - Add credentials in n8n as HTTP Header Auth with:
     - Name: `Authorization`
     - Value: `Bearer YOUR_API_KEY`

### Configuration

To customize the workflow:

- **Image Prompt**: Modify the prompt in the "Generate AI Image" node
- **Image Size**: Change the size parameter (default: 1024x1024)
- **Video Settings**: Adjust `cfg_scale` and `motion_bucket_id` in "Image to Video AI" node
- **Wait Time**: Modify the wait duration (default: 10 seconds)
- **Save Path**: Change the file path in "Save to File" node

### Usage

1. Click "Test workflow" button in n8n
2. The workflow will generate an image, convert it to video, and save it
3. Videos are saved to `/videos/` with timestamp filename

### Notes

- The workflow includes a polling loop that checks video status every 10 seconds
- Video generation can take several minutes depending on the API
- Make sure you have sufficient API credits for both OpenAI and Stability AI
- The workflow follows the structure visible in the provided screenshot

## Other Workflows in the Image

The screenshot also shows other workflows that could be created:
- **SHIFT 2 - Create Music** - AI music generation workflow
- **SHIFT 3 - Add Captions to Enhance Engagement** - Video captioning workflow
- **SHIFT 4 - Loop Video & Spotify** - Video/music looping workflow

Let me know if you'd like me to create any of these additional workflows!
