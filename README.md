# Dreambooth Ion Cannon

## Purpose

The Dreambooth Ion Cannon is a repository that abstracts away a large chunk of the execution pain points of [The Repo Formerly Known As Dreambooth](https://github.com/JoePenna/Dreambooth-Stable-Diffusion), providing a layperson an easily accessible guide to uploading photographs, training a Stable Diffusion model on said photographs, and generating images according to pre-selected prompts.

This repo (and _particularly_ this `README`) should be considered under active development until such time as this line of text disappears, so please pop in every so often in case things still appear piecemeal. I will be adding new prompts on occasion to the model (and have several ideas on how to smooth the path to training multi-subject models), so be aware that this is very much a construction zone.

After finishing the guide (again, active work if you're reading this line), I'll add some points on how to search for prompts and run them yourself using this repository - if you find any that you are particularly impressed with, [tag me on Twitter](https://twitter.com/functi0nZer0) with a screenshot as well as the prompt text and the seed, and I'll consider them for inclusion!

## Disclaimer

I must reiterate here - the _vast_ majority of this code is not my work.

This repository is a fork of a fork of a fork, with the original by Xavier Xiao found [here](https://github.com/XavierXiao/Dreambooth-Stable-Diffusion), the work of Joe Penna et al found [here](https://github.com/JoePenna/Dreambooth-Stable-Diffusion), and the work of Kane Wallmann found [here](https://github.com/KaneWallmann/Dreambooth-Stable-Diffusion).

In the interests of simplicity, I have removed all text in this README that is not directly related to how to use this repository. If you have issues with image quality etc, please read through Kane's repository (as it contains notes from all parties involved). There is a lot of wonderfully insightful stuff in there.

I am focusing the below 'how-to' on [Vast.AI](https://vast.ai) as the provisioning platform for GPU compute, simply because when I was trying this out, that was the platform that had resources available. Joe has asked folk to utilise RunPod [with his referral link](https://runpod.io/?ref=n8yfwyum), which allows him to continue his work without paying for it - if you're more technically inclined and feel confident that you can run a Jupyter notebook with Pytorch in a platform-agnostic manner, I strongly recommend you do so in order to show support.

## Controlling The Ion Cannon

This section is under live construction: if you're confused, come back in a bit - if you're still confused, ping me on Twitter and let me know what part you're struggling with!

- 0. You're going to want to sign up to [Vast.AI](https://vast.ai), log in, and add a payment method. I'm not going to hand-hold you through how to do that, it's a site a sophisticated UX and it uses Stripe and Crypto.com as its payment rails. I've been following Joe's advice and adding credit in US$10 increments - that will be more than enough for you to start.

![img.png](ion-cannon-images/Step0.PNG)

- 1. 
- ![img.png](ion-cannon-images/Step1.PNG)
- ![img.png](ion-cannon-images/Step2.PNG)
- ![img.png](ion-cannon-images/Step3.PNG)
- ![img.png](ion-cannon-images/Step4.PNG)
- ![img.png](ion-cannon-images/Step5.PNG)
- ![img.png](ion-cannon-images/Step6.PNG)
- ![img.png](ion-cannon-images/Step7.PNG)
- ![img.png](ion-cannon-images/Step8.PNG)
- ![img.png](ion-cannon-images/Step9.PNG)
- ![img.png](ion-cannon-images/Step10.PNG)
- ![img.png](ion-cannon-images/Step11.PNG)
- ![img.png](ion-cannon-images/Step12.PNG)
- ![img.png](ion-cannon-images/Step13.PNG)
- ![img.png](ion-cannon-images/Step14.PNG)
- ![img.png](ion-cannon-images/Step15.PNG)
- ![img.png](ion-cannon-images/Step16.PNG)
- ![img.png](ion-cannon-images/Step17.PNG)
- ![img.png](ion-cannon-images/Step18.PNG)
- ![img.png](ion-cannon-images/Step19.PNG)
- ![img.png](ion-cannon-images/Step20.PNG)

------------

# The Repo Formerly Known As "Dreambooth"
## ...now more accurately described as "Unfrozen Model Textual Inversion for Stable Diffusion"
![image](https://user-images.githubusercontent.com/100188076/192390551-cb89364f-af57-4aed-8f3d-f9eb9b61cf95.png)
, 
## <a name="notes-by-kane"></a>  Notes by Kane
 I have modified Joe's fork to take captions for the training set from the filename of the training image. This allows you
to train multiple people or things at the same time. It also takes the caption for the regularization images from the filename which allows you to regularize multi classes during 
the train as well. The results are seem quite good. 

It takes whatever is before an _ (underscore) in the file name and uses that as the caption on the image. (e.g. `caption_xyz.jpg`).

For your training images use something like `kwallmann man_001.jpg`. And for your regularization images use something like
`man_001.jpg`. You can have any number of different training image captions. I've only tried with 2 so far so there might
be issues if you try to do many more.

I've combined the `man_euler`, `person_ddim`, and `woman` regularization datasets into a single repository for convenience 
here: https://github.com/kanewallmann/Stable-Diffusion-Regularization-Images

Because the caption is taken solely from the filename, the parameter `--class_word` is no longer needed and no modifications to
`personalized.py` are required.


## <a name="notes-by-joe-penna"></a>  Notes by Joe Penna
### **INTRODUCTIONS!**
Hi! My name is Joe Penna.

You might have seen a few YouTube videos of mine under *MysteryGuitarMan*. I'm now a feature film director. You might have seen [ARCTIC](https://www.youtube.com/watch?v=N5aD9ppoQIo&t=6s) or [STOWAWAY](https://www.youtube.com/watch?v=A_apvQkWsVY).

For my movies, I need to be able to train specific actors, props, locations, etc. So, I did a bunch of changes to @XavierXiao's repo in order to train people's faces.

I can't release all the tests for the movie I'm working on, but when I test with my own face, I release those on my Twitter page - [@MysteryGuitarM](https://twitter.com/MysteryGuitarM).

Lots of these tests were done with a buddy of mine -- Niko from CorridorDigital. It might be how you found this repo!

I'm not really a coder. I'm just stubborn, and I'm not afraid of googling. So, eventually, some really smart folks joined in and have been contributing. In this repo, specifically: @djbielejeski @gammagec @MrSaad –– but so many others in our Discord!

This is no longer my repo. This is the people-who-wanna-see-Dreambooth-on-SD-working-well's repo!

Now, if you wanna try to do this... please read the warnings below first:

### **WARNING!**
- **This is bleeding edge stuff**... there is currently no easy way to run this. This repo is based on a repo based on another repo.
  - At the moment, it takes a LOT of effort to create something that's basically duct tape and bubble gum -- but eventually works SUPER well.
  - Step in, please! Don't let that scare ya -- but please know that you're wading through the jungle at night, with no torch...

- Unfreezing the model takes a lot of juice.
  - ~~You're gonna need an A6000 / A40 / A100 (or similar top-of-the-line thousands-of-dollars GPU).~~
  - You can now run this on a GPU with 24GB of VRAM (e.g. 3090). Training will be slower, and you'll need to be sure this is the *only* program running.
  - If, like myself, you don't happen to own one of those, I'm including a Jupyter notebook here to help you run it on a rented cloud computing platform. 
  - It's currently tailored to [runpod.io](https://runpod.io?ref=n8yfwyum), but can work on [vast.ai](#vast-ai-setup) / etc.
  
- This implementation does not fully implement Google's ideas on how to preserve the latent space.

  - Most images that are similar to what you're training will be shifted towards that.
  - e.g. If you're training a person, all people will look like you. If you're training an object, anything in that class will look like your object.

- There doesn't seem to be an easy way to train two subjects consecutively. You will end up with an `11-12GB` file before pruning.
  - The provided notebook has a pruner that crunches it down to `~2gb`
  
- Best practice is to change the token to a celebrity name. Here's [my wife trained with the exact same settings, except for the token](#using-the-generated-model)


# <a name="setup"></a> Setup
## <a name="easy-runpod-instructions"></a> Easy RunPod Instructions
- Sign up for RunPod. Feel free to use my [referral link here](https://runpod.io?ref=n8yfwyum), so that I don't have to pay for it (but you do).
- Click **Deploy** on either `SECURE CLOUD` or `COMMUNITY CLOUD`
- Follow these video instructions here:

[![VIDEO INSTRUCTIONS](https://img.youtube.com/vi/7m__xadX0z0/0.jpg)](https://www.youtube.com/watch?v=7m__xadX0z0#t=5m33.1s)

## <a name="vast-ai-setup"></a>  Vast.AI Instructions
- Sign up for [Vast.AI](https://vast.ai/)
- Add some funds (I typically add them in $10 increments)
- Navigate to the [Client - Create page](https://vast.ai/console/create/)
  - Select pytorch/pytorch as your docker image, and the buttons "Use Jupyter Lab Interface" and "Jupyter direct HTTPS"
  - ![img.png](readme-images/vast-ai-step1-select-docker-image.png)
- You will want to increase your disk space, and filter on GPU RAM (12gb checkpoint files + 4gb model file + regularization images + other stuff adds up fast)
  - I typically allocate 150GB
  - ![img.png](readme-images/vast-ai-step2-instance-filters.png)
  - Also good to check the Upload/Download speed for enough bandwidth so you don't spend all your money waiting for things to download.
- Select the instance you want, and click `Rent`, then head over to your [Instances](https://vast.ai/console/instances/) page and click `Open`
  - ![img.png](readme-images/vast-ai-step3-instances.png)
  - You will get an unsafe certificate warning. Click past the warning or install the [Vast cert](https://vast.ai/static/jvastai_root.cer).
- Click `Notebook -> Python 3` (You can do this next step a number of ways, but I typically do this)
  - ![img.png](readme-images/vast-ai-step4-get-repo.png)
- Clone Joe's repo with this command
  - `!git clone https://github.com/JoePenna/Dreambooth-Stable-Diffusion.git`
  - Click `run`
  - ![img.png](readme-images/vast-ai-step5-clone-repo.png)
- Navigate into the new `Dreambooth-Stable-Diffusion` directory on the left and open the `dreambooth_runpod_joepenna.ipynb` file
  - ![img.png](readme-images/vast-ai-step6-open-notebook.png)
- Follow the instructions in the workbook and start training

# <a name="text-vs-dreamb"></a>  Textual Inversion vs. Dreambooth
The majority of the code in this repo was written by Rinon Gal et. al, the authors of the Textual Inversion research paper.

A few bits about regularization images were added that we all thought were super important -- all the researchers included!

...until my images were trained under the class "dog":
<br><img src="https://media.discordapp.net/attachments/1024716296610385981/1024933960083587102/unknown.png" width="200">

...and under the nonsensical class "§¶•" instead of "man" or "woman" or "person":
<br><img src="https://media.discordapp.net/attachments/1024716296610385981/1024934146415529984/unknown.png" width="200">

...and with completely blank regularization images:
<br><img src="https://media.discordapp.net/attachments/1023293330601287711/1024933371102629898/IMG_7579.JPG" width="200">

And here's what `"photograph of an apple"` looked like before I messed with code a bit:
<br><img src="https://media.discordapp.net/attachments/1018943815370952855/1018946569850069052/unknown.png" width="200">

We're not realizing the "regularization class" bits of this code have no effect, and that there is little to no prior preservation loss.

So, out of respect to both the MIT team and the Google researchers, I'm renaming this fork to:
*"Unfrozen Model Textual Inversion for Stable Diffusion"*.

For an alternate implementation that attempts prior loss preservation, please see ["Alternate Option"](#hugging-face-diffusers) below.


# <a name="using-the-generated-model"></a> Using the generated model
The `ground truth` (real picture, caution: very beautiful woman)
<br><img src="https://user-images.githubusercontent.com/100188076/192403948-8d1d0e50-3e9f-495f-b8ba-1bcb6b536fc8.png" width="200">

Same prompt for all of these images below:

| `sks` | `woman` | `Natalie Portman` | `Kate Mara` |
| ----- | ------- | ----------------- | ----------- |
| <img src="https://user-images.githubusercontent.com/100188076/192403506-ab96c652-f7d0-47b0-98fa-267defa1e511.png" width="200"> | <img src="https://user-images.githubusercontent.com/100188076/192403491-cb258777-5091-4492-a6cc-82305fa729f4.png" width="200"> | <img src="https://user-images.githubusercontent.com/100188076/192403437-f9a93720-d41c-4334-8901-fa2d2a10fe36.png" width="200"> | <img src="https://user-images.githubusercontent.com/100188076/192403461-1f6972d9-64d0-46b0-b2ed-737e47aae31e.png" width="200"> |   

# <a name="debugging-your-results"></a> Debugging your results
### ❗❗ THE NUMBER ONE MISTAKE PEOPLE MAKE ❗❗

**Prompting with just your token. ie "joepenna" instead of "joepenna person"**


If you trained with `joepenna` under the class `person`, the model should only know your face as:

```
joepenna person
```

Example Prompts:

🚫 Incorrect (missing `person` following `joepenna`)
```
portrait photograph of joepenna 35mm film vintage glass
```

✅ This is right (`person` is included after `joepenna`)
```
portrait photograph of joepenna person 35mm film vintage glass
```

You might sometimes get someone who kinda looks like you with joepenna (especially if you trained for too many steps), but that's only because this current iteration of Dreambooth overtrains that token so much that it bleeds into that token.

---

#### ☢ Be careful with the types of images you train

While training, Stable doesn't know that you're a person. It's just going to mimic what it sees.

So, if these are your training images look like this:

![](readme-images/caution-training.png)

You're only going to get generations of you outside next to a spiky tree, wearing a white-and-gray shirt, in the style of... well, selfie photograph.

Instead, this training set is much better:

![](readme-images/better-training-images.png)

The only thing that is consistent between images is the subject. So, Stable will look through the images and learn only your face, which will make "editing" it into other styles possible.

## Oh no! You're not getting good generations!

#### <a name="they-dont-look-like-you"></a> OPTION 1: They're not looking like you at all! (Train longer, or get better training images)

Are you sure you're prompting it right?

It should be `<token> <class>`, not just `<token>`. For example:

`JoePenna person, portrait photograph, 85mm medium format photo`


If it still doesn't look like you, you didn't train long enough.

----

#### <a name="they-sorta-look-like-you-but-exactly-like-your-training-images"></a> OPTION 2: They're looking like you, but are all looking like your training images. (Train for less steps, get better training images, fix with prompting)

Okay, a few reasons why: you might have trained too long... or your images were too similar... or you didn't train with enough images.

No problem. We can fix that with the prompt. Stable Diffusion puts a LOT of merit to whatever you type first. So save it for later:

`an exquisite portrait photograph, 85mm medium format photo of JoePenna person with a classic haircut`


----

#### <a name="they-look-like-you-but-not-when-you-try-different-styles"></a> OPTION 3: They're looking like you, but not when you try different styles. (Train longer, get better training images)

You didn't train long enough...

No problem. We can fix that with the prompt:

`JoePenna person in a portrait photograph, JoePenna person in a 85mm medium format photo of JoePenna person`


### More tips and help here: [Stable Diffusion Dreambooth Discord](https://discord.com/invite/qbMuXBXyHA)

# <a name="hugging-face-diffusers"></a> Hugging Face Diffusers - Alternate Option

Note: This is a diffuser implementation, and use is much more complicated than using a *.ckpy file.

At the moment, there is no way to use the diffusers model with most repos (e.g. AUTOMATIC1111, HLKY, DeForum, etc)

Dreambooth is now supported in Hugging Face diffusers for training with stable diffusion, try it out in the colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/sd_dreambooth_training.ipynb)
