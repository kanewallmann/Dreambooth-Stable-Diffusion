import os
import numpy as np
import PIL
from PIL import Image
from torch.utils.data import Dataset
from torchvision import transforms
from pathlib import Path

class PersonalizedBase(Dataset):
    def __init__(self,
                 data_root,
                 size=None,
                 repeats=100,
                 interpolation="bicubic",
                 flip_p=0.0,
                 set="train",
                 center_crop=False,
                 reg=False
                 ):

        self.data_root = data_root

        self.image_paths = []

        classes = os.listdir(self.data_root)

        for cl in classes:
            class_path = os.path.join(self.data_root, cl)
            for file_path in os.listdir(class_path):
                if file_path.endswith(".png"):
                    image_path = os.path.join(class_path, file_path)
                    self.image_paths.append(image_path)

        # self._length = len(self.image_paths)
        self.num_images = len(self.image_paths)
        self._length = self.num_images

        self.center_crop = center_crop

        if set == "train":
            self._length = self.num_images * repeats

        self.size = size
        self.interpolation = {"linear": PIL.Image.LINEAR,
                              "bilinear": PIL.Image.BILINEAR,
                              "bicubic": PIL.Image.BICUBIC,
                              "lanczos": PIL.Image.LANCZOS,
                              }[interpolation]
        self.flip = transforms.RandomHorizontalFlip(p=flip_p)
        self.reg = reg

    def __len__(self):
        return self._length

    def __getitem__(self, i):
        example = {}
        image_path = self.image_paths[i % self.num_images]
        image = Image.open(image_path)

        if not image.mode == "RGB":
            image = image.convert("RGB")


        parts = image_path.split(".")
        parts.pop(len(parts)-1)
        parts.append("txt")
        captionpath = ".".join(parts)
        filecheck = Path(captionpath)
        identifier = ""
        if filecheck.exists():
            captionfile = open(captionpath,'r')
            identifier = captionfile.readline()
            captionfile.close()
        else:
            pathname = Path(image_path).name
            parts = pathname.split("_")
            identifier = parts[0]

        example["caption"] = identifier

        # default to score-sde preprocessing
        img = np.array(image).astype(np.uint8)

        if self.center_crop:
            crop = min(img.shape[0], img.shape[1])
            h, w, = img.shape[0], img.shape[1]
            img = img[(h - crop) // 2:(h + crop) // 2,
                      (w - crop) // 2:(w + crop) // 2]

        image = Image.fromarray(img)
        if self.size is not None:
            image = image.resize((self.size, self.size),
                                 resample=self.interpolation)

        image = self.flip(image)
        image = np.array(image).astype(np.uint8)
        example["image"] = (image / 127.5 - 1.0).astype(np.float32)
        return example
