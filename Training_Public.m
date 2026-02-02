n_training_images = 30;  % Total images to generate
train_threshold = 24;      % 8 for training
val_threshold = 3;        % 1 for validation (remaining 1 goes to test)

img_train_out_directory = 'C:\\Users\\shilp\\.AbhijeetProjectFiles\\Parking Lot Detector\\images\\train';
img_val_out_directory = 'C:\\Users\\shilp\\.AbhijeetProjectFiles\\Parking Lot Detector\\images\\val';
img_test_out_directory = 'C:\\Users\\shilp\\.AbhijeetProjectFiles\\Parking Lot Detector\\images\\test';

% Set random seed to get repeatable random numbers
rng(0)

% Configure geoaxes
h = figure;
grid off;
ax = geoaxes();
ax.Basemap = 'satellite';

% Starting position
% 38.85039088848158, -77.0447042011728

latitude0 = 38.85039088848158;
longitude0 = -77.0447042011728;

% Zoom to APL
geolimits(ax, [latitude0-0.01, latitude0+0.01], [longitude0-0.01, longitude0+0.01]);

% Generate a series of training images
for ii = 1:n_training_images
    % Move to a new place near APL
    lat_jitter = 0.001;
    lon_jitter = 0.001;
    % Approximate width of one image
    wlat = 0.0002;
    wlon = 0.0002;
    latitude = latitude0 + lat_jitter * rand() + [-1, 1]*wlat/2;
    longitude = longitude0 + lon_jitter * rand() + [-1, 1]*wlon/2;
    
    % Update coordinates
    geolimits(ax, latitude, longitude);
    
    ax.ZoomLevel = 21;
    
    % Get the image from the figure
    F = getframe(ax);
    
    % Determine which directory based on train/val/test split
    if ii <= train_threshold
        filename = sprintf('parking_image_train%d.png', ii);
        img_out_directory = img_train_out_directory;
    elseif ii <= train_threshold + val_threshold
        filename = sprintf('parking_image_val%d.png', ii - train_threshold);
        img_out_directory = img_val_out_directory;
    else
        filename = sprintf('parking_image_test%d.png', ii - train_threshold - val_threshold);
        img_out_directory = img_test_out_directory;
    end
    
    % Save the image to a file
    imwrite(F.cdata, fullfile(img_out_directory, filename));
    
    fprintf('Generated image %d/%d: %s\n', ii, n_training_images, filename);
end

fprintf('\nImage generation complete!\n');
fprintf('Training images: %d\n', train_threshold);
fprintf('Validation images: %d\n', val_threshold);
fprintf('Test images: %d\n', n_training_images - train_threshold - val_threshold);