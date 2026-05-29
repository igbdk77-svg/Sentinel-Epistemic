import torch
from sentinel import AdaptiveEpistemicSentinel

# 1. Sentinel'i başlat
sentinel = AdaptiveEpistemicSentinel(sensitivity=0.15)

# 2. Örnek bir model çıktısı (latent state) oluştur
latent_state = torch.randn(10, requires_grad=True)

# 3. Sentinel üzerinden geçir
safe_output = sentinel(latent_state)

print("Original latent state:", latent_state)
print("Safe (stabilized) output:", safe_output)
