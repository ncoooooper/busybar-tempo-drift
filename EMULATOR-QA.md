# Emulator verification

Interactive device controls and persistent local state on BUSY Bar firmware.

Recorded five beats and navigated to the measured difference between the two halves of the phrase.

29 distinct frames were recorded on firmware 1.3.1. App io.ncoooooper.tempodrift exited: finished; heap peak 80.8 of 128 KiB. Screenshots are in screenshots/ and the recording is in media/.

## Display capture

Firmware 1.3.1 rendered both README examples. Each square in a guide GIF is one front LED in a 16 × 16 cell. The production archive was built from the source in this repository.

## New mode

Two interactions were captured on firmware 1.3.1. Recorded source response. Back exited the app cleanly. See [recording details](media/source-mode-check.json).

## Screen transition capture

Firmware 1.3.1 rendered the display sequences in the README. The release archive also ran on a fresh emulator with rapid wheel reversals and Back during a transition. The guide uses a 14 × 14 lit area inside each 16 × 16 cell. Input sequences, frame counts and the release archive checksum are in [the capture record](media/screen-transitions.json).
