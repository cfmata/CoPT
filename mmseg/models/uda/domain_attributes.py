# Hand crafted domain templates
syn2real_domain_templates = {"a photo of a {}",
                            "a video game of a {}"}

# Real domain templates
real_domain_templates = {"{} that has fine details",
                        "{} that has natural colors and lighting",
                        "{} that is high resolution",
                        "{} that has depth and perspective",
                        "{} that has organic variation",
                        "{} that has complex textures",
                        "{} that has authentic shadows and reflections",
                        "{} with a blurred bokeh background",
                        "{} with a lens flare and glare",
                        "{} that has natural poses and expressions",
                        "{} that has environmental integration",
                        "{} that has realistic props and objects",
                        "{} that has accurate reflections in water and glass",
                        "{} that has natural compression artifacts",
                        "{} that shows weather and atmospheric effects",
                        "{} with unscripted candid moments",
                        "{} with a tangible sense of scale"}

# Synthetic domain templates
synthetic_domain_templates = {"{} with a lack of realism",
                            "{} that has unusual colors and lighting",
                            "{} with perfect symmetry",
                            "{} with repetitive elements",
                            "{} with a lack of organic variation",
                            "{} that has tiling and tiling artifacts",
                            "{} which is overly sharp or soft focus",
                            "{} that has inconsistent shadows and reflections",
                            "{} with distinctive noise patterns",
                            "{} that has regular patterns and grids",
                            "{} with a lack of depth and perspective",
                            "{} that looks like an inorganic object",
                            "{} in an artistic style or stylization",
                            "{} that has exaggerated features"}

# Daytime domain templates
daytime_domain_templates = {"{} with an abundance of natural light",
                            "{} with bright and vibrant colors",
                            "{} with soft shadows",
                            "{} with warmth in illumination",
                            "{} with dynamic range",
                            "{} with natural sky colors",
                            "{} with distinctive sun position",
                            "{} with clear visibility",
                            "{} with minimal artificial lighting",
                            "{} with lively and active atmosphere",
                            "{} with natural textures and patterns",
                            "{} with shimmering water bodies",
                            "{} with pleasant weather conditions",
                            "{} with outdoor shadows",
                            "{} with minimal noise and grain"}

# (CS2DZ & CS2ACDC) Nighttime domain templates
nighttime_domain_templates = {"{} with low light conditions",
                            "{} with dark shadows",
                            "{} with diminished color saturation",
                            "{} with warm artificial lighting",
                            "{} with contrast between light and dark",
                            "{} with point light sources",
                            "{} with visible light trails",
                            "{} with glowing skylines",
                            "{} with silhouettes and outlines",
                            "{} with noise and grain",
                            "{} with astrophotography elements",
                            "{} with long shadows",
                            "{} with reflective surfaces",
                            "{} with distant atmospheric haze",
                            "{} with a sense of mystery and atmosphere"}

# (CS2ACDC) Fog domain templates
foggy_domain_templates = {
    "{} with soft, diffused light",
    "{} with hazy atmosphere",
    "{} with low contrast",
    "{} with diminished sharpness and clarity",
    "{} with gradient of opacity",
    "{} with desaturation of colors",
    "{} with loss of detail in distance",
    "{} with diffused light sources",
    "{} with visible water droplets",
    "{} with muffled soundscape",
    "{} with ethereal and dreamlike atmosphere",
    "{} with silhouettes and silhouetted forms",
    "{} with moisture on surfaces",
    "{} with elongated shadows"
}

# (CS2ACDC) Rain domain templates
rainy_domain_templates = {
    "{} with raindrops on surfaces",
    "{} with wet and reflective surfaces",
    "{} with muted colors",
    "{} with glossy textures",
    "{} with diminished contrast",
    "{} with blurred backgrounds",
    "{} with dynamic water movement",
    "{} with puddles and reflections",
    "{} with umbrellas and rain gear",
    "{} with dramatic sky",
    "{} with wet vegetation",
    "{} with water ripples and disturbances",
    "{} with smeared or distorted lights",
    "{} with misty atmosphere"
}

# (CS2ACDC) Snow domain templates
snowy_domain_templates = {
    "{} with white blanket of snow",
    "{} with soft, diffused light",
    "{} with cool color palette",
    "{} with snowflakes in motion",
    "{} with crystalline texture",
    "{} with cold, wintry atmosphere",
    "{} with footprints and tracks",
    "{} with snow-covered trees and branches",
    "{} with icy surfaces and frozen water",
    "{} with winter clothing and gear",
    "{} with frost and ice crystals",
    "{} with blurred backgrounds and depth of field",
    "{} with cold breath and condensation",
    "{} with winter sports and activities"
}

def get_domain_templates(task):
    if task == 'gta2cs':
        return synthetic_domain_templates.union(real_domain_templates)
    elif task == 'synthia2cs':
        return synthetic_domain_templates.union(real_domain_templates)
    elif task == 'cs2acdc':
        return real_domain_templates.union(nighttime_domain_templates).union(
            foggy_domain_templates).union(rainy_domain_templates).union(snowy_domain_templates)
    elif task == 'cs2dz':
        return daytime_domain_templates.union(nighttime_domain_templates)
    else:
        raise Exception("Task ", task, " domain templates not implemented.")