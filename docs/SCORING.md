# Mathematical Virality Model

The virality of a track is defined as:
$$\text{Score} = (0.40 f_{\text{reuse}} + 0.25 c_{\text{channels}} + 0.20 t_{\text{spread}} + 0.15 \log(1 + v_{\text{views}})) \cdot M_{\text{category}} \cdot C_{\text{conf}}$$

### Shannon Entropy Dispersion
To defend against artificial Sybil upload spam:
$$H(C) = -\sum_{i=1}^k p(c_i) \log_2 p(c_i)$$
