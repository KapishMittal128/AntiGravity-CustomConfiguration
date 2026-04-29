---
name: remotion-video-template
description: A full, production-ready Remotion video component.
---

## Coffee SaaS Video Template
```tsx
import { AbsoluteFill, interpolate, useCurrentFrame, useVideoConfig } from 'remotion';

export const CoffeeVideo = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const opacity = interpolate(frame, [0, 30], [0, 1]);
  
  return (
    <AbsoluteFill style={{ backgroundColor: '#2C1B0E', justifyContent: 'center', alignItems: 'center' }}>
      <h1 style={{ color: '#F5E6D3', opacity, fontSize: 80 }}>BrewTrack SaaS</h1>
      <p style={{ color: '#F5E6D3', opacity, fontSize: 40 }}>Optimize your roast.</p>
    </AbsoluteFill>
  );
};
```