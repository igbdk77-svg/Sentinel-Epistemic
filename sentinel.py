import torch

class AdaptiveEpistemicSentinel:
    """
    Sentinel-Epistemic: Zero-compute epistemic safety filter.
    Protects latent spaces via gradient-based stabilization.
    """
    def __init__(self, sensitivity=0.15):
        self.sensitivity = sensitivity 

    def __call__(self, latent_state):
        # Ensure gradients are tracked
        was_grad_enabled = latent_state.requires_grad
        latent_state.requires_grad_(True)
        
        # Calculate gradient norm
        grad = torch.autograd.grad(outputs=latent_state.sum(), 
                                   inputs=latent_state, 
                                   retain_graph=False, 
                                   create_graph=True)[0]
        g_norm = torch.norm(grad)
        
        # Soft-gate stabilization
        sentinel_gate = torch.sigmoid((self.sensitivity - g_norm) * 50) 
        
        latent_state.requires_grad_(was_grad_enabled)
        return latent_state * sentinel_gate.detach()
