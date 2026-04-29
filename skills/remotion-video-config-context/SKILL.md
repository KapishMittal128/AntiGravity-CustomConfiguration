---
name: remotion-video-config-context
source_repo: remotion-dev/remotion
source_reference: packages/core/src/use-video-config.ts
---

# remotion-video-config-context

## Description
Extracts global composition properties to create relative, responsive animations that automatically scale with duration and resolution.

## Code Pattern
`const { fps, durationInFrames, width, height } = useVideoConfig();`

## Inputs
- Component requiring awareness of video context

## Outputs
- Relative animation calculations

## Dependencies
- Remotion
- React

## Execution Steps
1. Invoke `useVideoConfig()` to extract `fps` and `durationInFrames`.
2. Calculate animation exit points dynamically (e.g., `durationInFrames - 30`).
3. Use `fps` to configure exact `spring()` physics durations.
4. Scale internal component layouts based on `width` and `height`.
5. Eliminate hard-coded frame numbers for reusability.

## Example Usage
`Make the exit animation relative to the total duration using remotion-video-config-context.`
