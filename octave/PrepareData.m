ForestFires = csvread("forestfires.csv");
LogFromBurnedArea=log2(ForestFires(:,13)+ones(length(ForestFires), 1));
FireProbabilities = ForestFires(:,13)/max(ForestFires(:,13));
NewData = [ForestFires FireProbabilities];
csvwrite('fireprobs.csv', NewData);
Data = [ForestFires(:,1:12) LogFromBurnedArea];
