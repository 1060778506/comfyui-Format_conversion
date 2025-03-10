import os
import numpy as np
from PIL import Image
from pathlib import Path

class ImageFormatConverter:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),  # 传入的图像
                "format": (["jpg", "webp"],),  # 选择格式
                "quality": ("INT", {"default": 100, "min": 1, "max": 100}),  # 质量
            }
        }

    RETURN_TYPES = ("IMAGE", "STRING")  # 返回转换后的图片和文件路径
    FUNCTION = "convert_image"
    CATEGORY = "Image Processing"

    def convert_image(self, image, format, quality):
        # 处理图像数据（转换为 uint8 格式）
        image = (image * 255).astype("uint8")

        # 创建 Pillow 图像并转换为 RGB 模式
        img = Image.fromarray(image).convert("RGB")

        # 确保保存目录存在
        output_dir = Path(os.getcwd()) / "output_images"
        output_dir.mkdir(parents=True, exist_ok=True)

        # 生成文件路径
        save_path = output_dir / f"converted_image.{format}"

        # 保存图像
        img.save(save_path, format.upper(), quality=quality)

        return np.array(img) / 255.0, str(save_path)  # 返回新图像和路径

NODE_CLASS_MAPPINGS = {
    "ImageFormatConverter": ImageFormatConverter
}
