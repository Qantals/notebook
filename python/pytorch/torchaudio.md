```py
# torchinfo
from torchinfo import summary
summary(model(), input_size=(1,28,28),device='cpu')


# torchaudio
    # load
import torchaudio
waveform, sample_rate = torchaudio.load(filename, num_frames=3, frame_offset =2)
    # ipython, matplotlib
import IPython.display as ipd
ipd.Audio(waveform.numpy(), rate=sample_rate)
plt.plot(waveform.t().numpy())
plt.imshow(yes_spectrogram.log2()[0,:,:].numpy(), cmap='viridis') # x-axis: time, y-axis: frequency
    # transforms
torchaudio.transforms.Resample(sample_rate, new_sample_rate)(waveform[channel,:].view(1,-1))
torchaudio.transforms.Spectrogram()(waveform_classA)
torchaudio.transforms.MelSpectrogram(sample_rate)(waveform)
torchaudio.transforms.MFCC(sample_rate)(waveform)


# lr rate
schedule = optim.lr_scheduler.StepLR(optimizer, step_size, gamma, last_epoch=-1)
lr_1 = optimizer.param_groups[0]['lr']
schedule.step()






```
