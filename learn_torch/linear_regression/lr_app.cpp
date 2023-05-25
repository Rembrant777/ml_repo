#include <torch/torch.h>

int main () {
    // first generate random input data 
    auto x = torch::randn({100, 1}); 
    auto y = 2 * x + 0.5 * torch::randn_like(x); 

    // define a linear regression model 
    torch::nn::Linear model(1,1); 

    // define a mean squared error (mse) loss function 
    torch::nn::MSELoss loss_fn; 

    // define an optimizer (e.g., Stochastic Gradient Descent)
    torch::optim::SGD optimizer(model->parameters(), /* learning_rate */ 0.1);

    // train the model
    for (int epoch = 0; epoch < 100; ++epoch) {
        // forward pass 
        auto y_pred = model(x); 
        auto loss = loss_fn(y_pred, y);
    
       // backward pass and optimization 
       optimizer.zero_grad(); 
       loss.backward(); 
       optimizer.step();

       // here print predicted value of y every 10 epoch 
       if (epoch % 10 == 0) {
           std::cout << "Epoch " << epoch << ", Predicted values: " << y_pred << std::endl; 
       } 
    }

    std::cout << "here are the output model " << std::endl; 
    torch::Tensor output_weights = model->weight; 
    torch::Tensor output_bias = model->bias;


    std::cout << "weight output size value " << output_weights.sizes() << std::endl; 
    std::cout << "bias output size value " << output_bias.sizes() << std::endl; 
    return 0; 
}

