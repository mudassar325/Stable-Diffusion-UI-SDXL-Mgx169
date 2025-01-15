import os

# Update and install NVIDIA driver
os.system(f"apt search nvidia-driver")
os.system(f"apt install nvidia-driver-535-server nvidia-dkms-535-server -y")

# Navigate to the app directory
os.chdir(f"/home/xlab-app-center")

# Clone the repository for the stable-diffusion-webui
os.system(f"git clone https://github.com/vladmandic/automatic /home/xlab-app-center/stable-diffusion-webui")

# Change to the stable-diffusion-webui directory
os.chdir(f"/home/xlab-app-center/stable-diffusion-webui")

# Clone necessary extensions and other components
extensions = [
    "https://github.com/etherealxx/batchlinks-webui",
    "https://github.com/deforum-art/deforum-for-automatic1111-webui",
    "https://github.com/AlUlkesh/stable-diffusion-webui-images-browser",
    "https://github.com/zanllp/sd-webui-infinite-image-browsing",
    "https://github.com/camenduru/stable-diffusion-webui-huggingface",
    "https://github.com/camenduru/sd-civitai-browser",
    "https://github.com/kohya-ss/sd-webui-additional-networks",
    "https://github.com/Mikubill/sd-webui-controlnet",
    "https://github.com/fkunn1326/openpose-editor",
    "https://github.com/jexom/sd-webui-depth-lib",
    "https://github.com/hnmr293/posex",
    "https://github.com/nonnonstop/sd-webui-3d-open-pose-editor",
    "https://github.com/camenduru/sd-webui-tunnels",
    "https://github.com/camenduru/sd_webui_stealth_pnginfo",
    "https://github.com/camenduru/sd-webui-aspect-ratio-helper",
]

# Clone all extensions into the web UI extensions folder
for extension in extensions:
    os.system(f"git clone {extension} /home/xlab-app-center/stable-diffusion-webui/extensions/")

# Install git-lfs
os.system(f"git lfs install")

# Reset the repository to ensure it's up-to-date
os.system(f"git reset --hard")

# Clone specific embeddings and models
os.system(f"git clone https://huggingface.co/embed/negative /home/xlab-app-center/stable-diffusion-webui/embeddings/negative")
os.system(f"git clone https://huggingface.co/embed/lora /home/xlab-app-center/stable-diffusion-webui/models/Lora/positive")

# Download models using aria2c
model_urls = [
    ("https://huggingface.co/CrucibleAI/ControlNetMediaPipeFace/resolve/main/control_v2p_sd15_mediapipe_face.yaml", "/home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-controlnet/models"),
    ("https://huggingface.co/CrucibleAI/ControlNetMediaPipeFace/resolve/main/control_v2p_sd15_mediapipe_face.safetensors", "/home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-controlnet/models"),
    ("https://huggingface.co/monster-labs/control_v1p_sd15_qrcode_monster/resolve/main/v2/control_v1p_sd15_qrcode_monster_v2.yaml", "/home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-controlnet/models"),
    ("https://huggingface.co/monster-labs/control_v1p_sd15_qrcode_monster/resolve/main/v2/control_v1p_sd15_qrcode_monster_v2.safetensors", "/home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-controlnet/models"),
    ("https://huggingface.co/CiaraRowles/TemporalNet/resolve/main/cldm_v15.yaml", "/home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-controlnet/models"),
    ("https://huggingface.co/CiaraRowles/TemporalNet/resolve/main/diff_control_sd15_temporalnet_fp16.safetensors", "/home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-controlnet/models"),
    ("https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11e_sd15_ip2p_fp16.safetensors", "/home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-controlnet/models"),
    ("https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11e_sd15_shuffle_fp16.safetensors", "/home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-controlnet/models"),
    ("https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_canny_fp16.safetensors", "/home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-controlnet/models"),
    ("https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11f1p_sd15_depth_fp16.safetensors", "/home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-controlnet/models"),
    ("https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_inpaint_fp16.safetensors", "/home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-controlnet/models"),
    ("https://huggingface.co/ckpt/ControlNet-v1-1/resolve/main/control_v11p_sd15_lineart_fp16.safetensors", "/home/xlab-app-center/stable-diffusion-webui/extensions/sd-webui-controlnet/models"),
]

# Download all model files using aria2c
for url, save_path in model_urls:
    os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M --async-dns=false {url} -d {save_path} -o {url.split('/')[-1]}")

# Install additional dependencies if required
os.system(f"apt install git-lfs")

# Clean up and finalize setup
os.system(f"sudo apt update -y")
os.system(f"sudo apt upgrade -y")

print("Setup and model updates completed successfully.")
